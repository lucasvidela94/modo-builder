---
name: item-bloque-mob
description: Write the item, block or mob JSON for a Bedrock add-on, plus its texture index entry, language name and recipe. Use once plan.md has a confirmed idea to build.
---

# Item, bloque o mob

**Criterio de cierre:** cada archivo que el paso del plan pide existe, tiene el `namespace` de
`config.json`, su textura está registrada en el índice, su nombre está en el idioma, y `probar`
corrió sin errores. Los componentes exactos están en `references/componentes.md`.

## Antes de empezar

1. Leé `plan.md` y decí en una frase qué se va a construir.
2. Verificá que existan `addon/config.json` y los dos packs; si falta alguno, corré `addon-base`.
3. Tomá el `namespace` y la versión de `config.json`. El identificador es siempre
   `namespace:nombre_en_minusculas` (`miaddon:rayo_espada`).

## Item

`addon/behavior_packs/mi_addon_bp/items/rayo_espada.json`:

```json
{
  "format_version": "1.26.50",
  "minecraft:item": {
    "description": {
      "identifier": "miaddon:rayo_espada",
      "menu_category": { "category": "equipment" }
    },
    "components": {
      "minecraft:max_stack_size": 1,
      "minecraft:durability": { "max_durability": 500 },
      "minecraft:icon": "miaddon:rayo_espada",
      "minecraft:hand_equipped": true
    }
  }
}
```

`components` tiene que estar presente aunque quede vacío. `format_version` es la versión de
definiciones de `config.json`, no la del pack.

El `minecraft:icon` apunta al nombre corto de la textura, que se registra en
`resource_packs/mi_addon_rp/textures/item_texture.json`:

```json
{
  "texture_data": {
    "miaddon:rayo_espada": { "textures": "textures/items/rayo_espada" }
  }
}
```

Cada item nuevo suma una entrada a `texture_data`. Las anteriores se quedan donde están.

## Nombre visible

En `resource_packs/mi_addon_rp/texts/es_ES.lang`, una línea por cada cosa:

```
item.miaddon:rayo_espada=Espada de rayo
tile.miaddon:cobre_bloque.name=Bloque de cobre
```

Los items llevan `item.<id>=Nombre` y los bloques `tile.<id>.name=Nombre`. El archivo
`texts/languages.json` tiene que listar `["es_ES"]`; creálo con eso si no existe.

## Bloque

`addon/behavior_packs/mi_addon_bp/blocks/cobre_bloque.json`, con `minecraft:block`, el identificador
y los componentes que el plan pida: `minecraft:destructible_by_mining` para lo que tarda en
romperse, `minecraft:material_instances` y `minecraft:geometry` para cómo se ve. La textura va en
`textures/blocks/` y se registra en `textures/terrain_texture.json`, igual que en el item.

## Mob

`addon/behavior_packs/mi_addon_bp/entities/`, con `minecraft:entity` e identificador propio. Un mob
sale de un **molde**: copiá la definición de un mob de vanilla parecido (un cerdo, una vaca), y
cambiá identificador, vida, velocidad y soltado. Las formas y animaciones van con
`texturas-y-modelos`.

## Receta (si el plan la pide)

`addon/behavior_packs/mi_addon_bp/recipes/`, con `minecraft:recipe_shaped` o
`minecraft:recipe_shapeless` y el resultado apuntando al identificador del item. El `format_version`
de una receta es `"1.20.10"`: las recetas quedaron en esa versión y no se actualizan con el juego.

## Reglas

- Antes de crear un archivo, buscá si ya existe uno con ese nombre: si está, lo estás por pisar.
- Después de crear o tocar archivos, corré `probar`.
- Un componente que no esté en `references/componentes.md` se verifica en la documentación de la
  versión del proyecto antes de escribirlo.
- Lo que el JSON no puede hacer (efectos, contadores, reacciones) va a `scripts-avanzados`, y se lo
  decís a la persona como una segunda etapa.
