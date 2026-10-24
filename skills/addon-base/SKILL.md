---
name: addon-base
description: Create the behavior pack and resource pack structure of a Bedrock add-on, with both manifests, linked UUIDs and the project's fixed versions. Use at the start of a project, or when the structure or config.json is missing.
---

# Add-on base

**Criterio de cierre:** `addon/config.json` existe con la versión del juego fijada, los dos packs
tienen su `manifest.json` con UUID propios, y el behavior pack declara como dependencia el UUID del
resource pack. Los números exactos y las reglas de UUID están en `references/manifest.md`.

## Paso 1: fijar la versión del juego

`addon/config.json` es la fuente de verdad de la versión del proyecto: las demás skills la leen de
ahí. Si no existe, creálo:

```json
{
  "namespace": "miaddon",
  "nombre": "Mi Add-on",
  "descripcion": "Add-on creado con Modo Builder",
  "minecraft": "1.26.50",
  "script_api": "2.9.0"
}
```

- `namespace`: prefijo de todos los identificadores (`miaddon:rayo_espada`). Minúsculas, números y
  guiones bajos.
- `minecraft`: la versión **instalada por la persona**, en formato `1.26.50`. Confirmala antes de
  escribirla (ver "Versión del juego" en `references/manifest.md`) y avisá que el proyecto queda
  fijado ahí.
- `script_api`: la versión estable de `@minecraft/server`. Sólo se usa si el plan pide scripts.

Preguntá la versión una vez, al principio. Cambiarla después obliga a repasar todos los archivos.

## Paso 2: crear la estructura

```
addon/
  config.json
  behavior_packs/mi_addon_bp/
    manifest.json
    items/  blocks/  entities/  recipes/  loot_tables/
  resource_packs/mi_addon_rp/
    manifest.json
    textures/items/  textures/blocks/
    texts/es_ES.lang
    texts/languages.json
```

Las carpetas vacías no son un problema: Minecraft las ignora hasta que tengan contenido.

## Paso 3: los dos manifest

Generá **cuatro UUID distintos** (header y módulo de cada pack):

```
python3 -c "import uuid; print(uuid.uuid4())"
```

- `behavior_packs/mi_addon_bp/manifest.json`: `header` con `name`, `description`, `uuid`,
  `version`, `min_engine_version`; un módulo `type: "data"`; y en `dependencies` el **UUID del
  header del resource pack**.
- `resource_packs/mi_addon_rp/manifest.json`: igual, con un módulo `type: "resources"` y sin
  dependencias.

`min_engine_version` sale de `config.json` partido en tres números (`"1.26.50"` → `[1, 26, 50]`).
La plantilla completa, lista para completar, está en `references/manifest.md`.

## Paso 4: contarle a la persona

Una frase, sin jerga: qué se creó y que el paso siguiente es el primer item. Nada de UUIDs ni de
nombres de carpetas: eso es tuyo.
