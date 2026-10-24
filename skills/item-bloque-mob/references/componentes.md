# Componentes verificados

Material de consulta de `item-bloque-mob`. Todos los nombres de esta lista están verificados contra
la documentación de Bedrock 1.26.50 (octubre 2026). Los que cambiaron de nombre en versiones
recientes están marcados: si el proyecto apunta a una versión vieja, el nombre viejo es el correcto.

## Item

| Componente | Para qué | Nota |
| --- | --- | --- |
| `minecraft:icon` | La textura del item | Es un **string** con el nombre corto registrado en `item_texture.json`. La forma `{"texture": ...}` es de versiones viejas |
| `minecraft:max_stack_size` | Cuántos se apilan | Default 64; los que se gastan van en 1 |
| `minecraft:durability` | Aguante del item | `{"max_durability": 500}`. Antes era `minecraft:max_damage` |
| `minecraft:damage` | Daño que pega | Número. Antes era `minecraft:attack_damage` |
| `minecraft:hand_equipped` | Se ve en la mano | `true` para espadas y herramientas |
| `minecraft:food` | Comida | `{"nutrition": 4, "saturation_modifier": 0.6}` |
| `minecraft:use_animation` | Animación al usarlo | `"eat"`, `"drink"`, `"bow"` |
| `minecraft:glint` | Brillo de encantado | `true` |
| `minecraft:foil` | Brillo tipo papel | `true` |

Categorías de `menu_category.category`: `construction`, `equipment`, `items`, `nature`, `none`.

## Bloque

| Componente | Para qué | Nota |
| --- | --- | --- |
| `minecraft:destructible_by_mining` | Cuánto tarda en romperse | `{"seconds_to_destroy": 3}`. Antes era `minecraft:destroy_time` |
| `minecraft:destructible_by_explosion` | Resistencia a explosiones | `{"explosion_resistance": 3}` |
| `minecraft:geometry` | La forma | `"minecraft:geometry.full_block"` para el cubo normal |
| `minecraft:material_instances` | Las texturas por cara | `{"*": {"texture": "miaddon:bloque"}}`; con `down`/`up`/`north`/`east`/`south`/`west` se hace por cara |
| `minecraft:loot` | Qué suelta | Ruta a la loot table; sin esto, el bloque se suelta a sí mismo |
| `minecraft:light_emission` | Luz que emite | 0 a 15 |
| `minecraft:map_color` | Color en el mapa | Hex, `"#ffffff"` |
| `minecraft:sound` | Sonido al pisarlo o romperlo | `{"sound": "grass"}` |

El bloque no tiene definición en el resource pack: su textura se registra en
`textures/terrain_texture.json`.

## Entidad (mob)

Los componentes son muchos y dependen del comportamiento buscado (caminar, nadar, volar, atacar). Por
eso la vía es el **molde**: copiá la definición de vanilla más parecida y cambiá lo propio.
Referencia completa: <https://wiki.bedrock.dev/entities/entity-intro> y
<https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/entitycomponentsintro>

Los tres ajustes que casi siempre hacen falta:

- `minecraft:health`: `{"value": 20, "max": 20}`
- `minecraft:movement`: `{"value": 0.25}`
- `minecraft:type_family`: las familias a las que pertenece (`["miaddon:dragon"]`)

## Recetas

`format_version` de `"1.20.10"` para `minecraft:recipe_shaped` y `minecraft:recipe_shapeless`. Es de
las pocas definiciones que no siguen la versión del juego.

## Textos

- Item: `item.<namespace>:<id>=Nombre visible`
- Bloque: `tile.<namespace>:<id>.name=Nombre visible`

Sin el `.name` en items y con él en bloques: es la convención de la plataforma, no un descuido.

## Documentación

- Items: <https://wiki.bedrock.dev/items/items-intro>
- Bloques: <https://wiki.bedrock.dev/blocks/blocks-intro>
- Lista completa de componentes (oficial):
  <https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/>
  y <https://learn.microsoft.com/en-us/minecraft/creator/reference/content/blockreference/>
