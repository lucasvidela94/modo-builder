#!/usr/bin/env python3
"""Empaqueta el add-on en un .mcaddon, desde la raíz del proyecto.

Deja `dist/mi_addon.mcaddon` con `behavior_packs/` y `resource_packs/` en la raíz del zip, que es
lo que Minecraft espera. Anda igual en Windows, macOS y Linux: no depende de PowerShell.

    python3 skills/probar/scripts/empaquetar.py [nombre]
"""

from __future__ import annotations

import pathlib
import sys
import zipfile

RAIZ = pathlib.Path("addon")
CARPETAS = ("behavior_packs", "resource_packs")


def main() -> int:
    if not RAIZ.is_dir():
        print("✘ No encuentro la carpeta addon/. Corré esto desde la raíz del proyecto.")
        return 1

    nombre = (sys.argv[1] if len(sys.argv) > 1 else "mi_addon").removesuffix(".mcaddon")
    salida = pathlib.Path("dist") / f"{nombre}.mcaddon"
    salida.parent.mkdir(parents=True, exist_ok=True)

    archivos = [
        f
        for carpeta in CARPETAS
        for f in sorted((RAIZ / carpeta).rglob("*"))
        if f.is_file()
    ]
    if not archivos:
        print("✘ No hay archivos en behavior_packs/ ni resource_packs/: nada que empaquetar.")
        return 1

    try:
        with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
            for f in archivos:
                z.write(f, f.relative_to(RAIZ))
    except PermissionError:
        print(f"✘ No pude escribir {salida}. Cerrá Minecraft si lo tiene abierto y reintentá.")
        return 1

    kb = salida.stat().st_size / 1024
    print(f"✔ {salida} ({len(archivos)} archivos, {kb:.0f} KB)")
    print("  Abrila con doble clic para cargarla en Minecraft.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
