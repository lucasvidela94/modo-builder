#!/usr/bin/env python3
"""Revisa un add-on de Minecraft Bedrock antes de empaquetarlo.

Corre desde la raíz del proyecto (donde vive `addon/`). Sin dependencias: sólo la biblioteca
estándar, para que ande igual en Windows, macOS y Linux.

    python3 skills/probar/scripts/revisar.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

RAIZ = pathlib.Path("addon")
UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

problemas: list[str] = []
avisos: list[str] = []


def problema(msg: str) -> None:
    problemas.append(msg)


def aviso(msg: str) -> None:
    avisos.append(msg)


def main() -> int:
    if not RAIZ.is_dir():
        print("✘ No encuentro la carpeta addon/. Corré esto desde la raíz del proyecto.")
        return 1

    todos = revisar_sintaxis()
    # Los manifest, items y bloques son objetos; languages.json es una lista.
    objetos = {k: v for k, v in todos.items() if isinstance(v, dict)}

    namespace = str(leer_config().get("namespace", ""))
    revisar_manifests(objetos)
    revisar_identificadores(objetos, namespace)
    revisar_imagenes(objetos)
    revisar_idioma(objetos, todos)

    for a in avisos:
        print(f"! {a}")
    for p in problemas:
        print(f"✘ {p}")

    if problemas:
        print(f"\n{len(problemas)} problema(s): se arreglan antes de empaquetar.")
        return 1

    print("\n✔ Todo parsea y cada referencia resuelve. Listo para empaquetar.")
    return 0


def leer_config() -> dict:
    ruta = RAIZ / "config.json"
    if not ruta.is_file():
        aviso("Falta addon/config.json: corré la skill addon-base para fijar namespace y versión.")
        return {}
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def revisar_sintaxis() -> dict[pathlib.Path, object]:
    """Lee todos los JSON. Devuelve {ruta relativa a addon/: contenido}."""
    cargados: dict[pathlib.Path, object] = {}
    for ruta in sorted(RAIZ.rglob("*.json")):
        rel = ruta.relative_to(RAIZ)
        try:
            cargados[rel] = json.loads(ruta.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            problema(f"{ruta}: JSON roto en la línea {e.lineno}, columna {e.colno} ({e.msg}).")
        except UnicodeDecodeError:
            problema(f"{ruta}: no es texto UTF-8.")
    print(f"· {len(cargados)} archivo(s) JSON leídos")
    return cargados


def revisar_manifests(objetos: dict[pathlib.Path, dict]) -> None:
    """Cada manifest con UUID válido y único; el BP declarando al RP."""
    vistos: dict[str, str] = {}
    bp_uuid = rp_uuid = None

    for ruta, datos in objetos.items():
        if ruta.name != "manifest.json":
            continue
        header = datos.get("header") or {}
        es_bp = "behavior_packs" in ruta.parts

        if datos.get("format_version") != 2:
            problema(f"{ruta}: format_version tiene que ser 2.")

        roles = [("header", header.get("uuid"))]
        roles += [("módulo", m.get("uuid")) for m in datos.get("modules") or [] if isinstance(m, dict)]
        for rol, u in roles:
            if not u or not UUID_RE.match(str(u).lower()):
                problema(f"{ruta}: el uuid de {rol} está vacío o mal formado.")
                continue
            if u in vistos:
                problema(f"{ruta}: el uuid de {rol} ya lo usa {vistos[u]}. Cada uno es único.")
            vistos[str(u)] = f"{ruta} ({rol})"

        if not header.get("min_engine_version"):
            problema(f"{ruta}: falta min_engine_version en el header.")
        if not header.get("version"):
            problema(f"{ruta}: falta version en el header del pack.")

        if es_bp:
            bp_uuid = header.get("uuid")
        else:
            rp_uuid = header.get("uuid")

    if not bp_uuid or not rp_uuid:
        return

    for ruta, datos in objetos.items():
        if ruta.name != "manifest.json" or "behavior_packs" not in ruta.parts:
            continue
        deps = [str(d.get("uuid")) for d in datos.get("dependencies") or [] if isinstance(d, dict)]
        if rp_uuid not in deps:
            problema(
                f"{ruta}: dependencies no incluye el uuid del resource pack ({rp_uuid}). "
                "Sin eso los visuales no se enlazan."
            )
        for d in deps:
            if d != rp_uuid and d not in vistos:
                aviso(f"{ruta}: depende de un uuid que no está en este proyecto ({d}).")


def revisar_identificadores(objetos: dict[pathlib.Path, dict], namespace: str) -> None:
    if not namespace:
        return
    prefijo = f"{namespace}:"
    for ruta, datos in objetos.items():
        if ruta.name in ("manifest.json", "config.json"):
            continue
        definicion = datos.get("minecraft:item") or datos.get("minecraft:block")
        if not isinstance(definicion, dict):
            continue
        ident = str((definicion.get("description") or {}).get("identifier", ""))
        if not ident.startswith(prefijo):
            problema(f"{ruta}: el identificador '{ident}' tiene que empezar con '{prefijo}'.")
        if ident != ident.lower():
            problema(f"{ruta}: el identificador '{ident}' lleva mayúsculas.")
        if "components" not in definicion:
            problema(f"{ruta}: falta la sección components (aunque quede vacía).")


def revisar_imagenes(objetos: dict[pathlib.Path, dict]) -> None:
    """Cada textura del índice tiene su PNG; cada PNG del proyecto está declarado."""
    declarados: set[str] = set()

    for ruta, datos in objetos.items():
        if not str(ruta).endswith("_texture.json"):
            continue
        for corto, entrada in (datos.get("texture_data") or {}).items():
            destino = entrada.get("textures") if isinstance(entrada, dict) else None
            if not destino:
                problema(f"{ruta}: '{corto}' no apunta a ninguna textura.")
                continue
            if not str(destino).startswith("textures/"):
                aviso(f"{ruta}: '{corto}' debería usar la forma 'textures/items/nombre'.")
            declarados.add(str(destino).removeprefix("textures/"))
            png = RAIZ / ruta.parent.parent / f"{destino}.png"
            if not png.is_file():
                problema(f"{ruta}: '{corto}' apunta a {destino}.png y ese archivo no existe.")

    for png in RAIZ.glob("resource_packs/*/textures/**/*.png"):
        partes = png.parts
        if "resource_packs" not in partes:
            continue
        # resource_packs/<pack>/textures/items/x.png -> items/x
        rel = "/".join(partes[partes.index("resource_packs") + 3 :]).rsplit(".", 1)[0]
        if rel not in declarados:
            aviso(f"{png.name}: el PNG existe pero ningún índice lo declara.")
        if png.name != png.name.lower() or " " in png.name:
            problema(f"{png.name}: el nombre lleva mayúsculas o espacios; Minecraft no lo lee.")


def revisar_idioma(objetos: dict[pathlib.Path, dict], todos: dict[pathlib.Path, object]) -> None:
    for ruta, datos in todos.items():
        if ruta.name != "languages.json":
            continue
        if isinstance(datos, list):
            if "es_ES" not in datos:
                aviso(f"{ruta}: no lista es_ES; los nombres en castellano no van a aparecer.")
        else:
            aviso(f"{ruta}: debería ser una lista, como [\"es_ES\"].")

    ids = set()
    for ruta, datos in objetos.items():
        if ruta.name == "manifest.json":
            continue
        for clave in ("minecraft:item", "minecraft:block"):
            definicion = datos.get(clave)
            if isinstance(definicion, dict):
                ident = (definicion.get("description") or {}).get("identifier")
                if ident:
                    ids.add(str(ident))
    if not ids:
        return

    for ruta in RAIZ.glob("resource_packs/*/texts/*.lang"):
        claves = set()
        for linea in ruta.read_text(encoding="utf-8").splitlines():
            if "=" in linea and not linea.strip().startswith("#"):
                clave = linea.split("=", 1)[0].strip()
                # item.<id>=Nombre  /  tile.<id>.name=Nombre  ->  <id>
                if clave.startswith(("item.", "tile.")):
                    clave = clave.split(".", 1)[1].removesuffix(".name")
                claves.add(clave)
        for ident in sorted(ids):
            if ident not in claves:
                problema(f"{ruta}: falta el nombre visible de '{ident}'.")


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # noqa: BLE001 - queremos el mensaje crudo para explicarlo
        print(f"✘ El revisar falló: {type(e).__name__}: {e}")
        sys.exit(1)
