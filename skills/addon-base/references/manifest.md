# Manifest y versiones

Material de consulta de `addon-base`. Leelo al crear la estructura y cada vez que cambie la versión
del proyecto.

## Versión del juego

Antes de escribir un número acá, confirmá cuál es la versión instalada de la persona. Tres formas,
de la más rápida a la más segura:

1. Preguntale: en el menú principal de Minecraft, abajo a la derecha, dice el número (por ejemplo
   `v1.26.52`).
2. Si el juego está en Windows, el número de versión aparece en Microsoft Store → Minecraft →
   detalles.
3. Consultá la versión retail actual en <https://minecraft.wiki/w/Bedrock_Edition> o
   <https://www.minecraft.net/en-us/download> y usá esa.

La regla de la plataforma oficial ("N o N-1") es que un add-on escrito para la versión menor actual
o la anterior está al día. Un proyecto escrito para una versión más vieja sigue funcionando, pero no
puede usar los componentes nuevos.

**Verificado en octubre de 2026:** retail **1.26.52** (25/09/2026); `format_version` de las
definiciones de item, bloque y entidad **`"1.26.50"`**; la línea anterior era 1.21.x. Cuando la
versión del juego cambie, actualizá el `"minecraft"` de `config.json`, el `min_engine_version` de
los manifest y el `format_version` de las definiciones nuevas.

## Reglas del manifest

- `format_version`: **2** para behavior packs y resource packs. (La 3 existe en preview y todavía no
  se usa. La 1 es sólo para skin packs.)
- `min_engine_version`: `[major, minor, patch]` del juego. Un valor por encima del juego instalado
  hace que el pack no cargue.
- `version`: `[major, minor, patch]` del pack. Empezá en `[1, 0, 0]` y subilo en los cambios
  grandes: Minecraft reemplaza el pack viejo sólo si la versión es mayor.
- Cada `uuid` tiene formato `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` y es único en el mundo. Cuatro
  UUID nuevos por proyecto: header y módulo de cada pack.
- El behavior pack declara en `dependencies` el `uuid` del **header** del resource pack, con la
  misma `version`.
- Los módulos: `type: "data"` para el comportamiento, `"resources"` para los visuales, y `"script"`
  (con `language: "javascript"` y `entry`) cuando el proyecto usa Script API.

## Plantilla del behavior pack

```json
{
  "format_version": 2,
  "header": {
    "name": "Mi Add-on (comportamiento)",
    "description": "Comportamiento del add-on",
    "uuid": "UUID-HEADER-BP",
    "version": [1, 0, 0],
    "min_engine_version": [1, 26, 50]
  },
  "modules": [
    { "type": "data", "uuid": "UUID-MODULO-BP", "version": [1, 0, 0] }
  ],
  "dependencies": [
    { "uuid": "UUID-HEADER-RP", "version": [1, 0, 0] }
  ]
}
```

## Plantilla del resource pack

```json
{
  "format_version": 2,
  "header": {
    "name": "Mi Add-on (visuales)",
    "description": "Visuales del add-on",
    "uuid": "UUID-HEADER-RP",
    "version": [1, 0, 0],
    "min_engine_version": [1, 26, 50]
  },
  "modules": [
    { "type": "resources", "uuid": "UUID-MODULO-RP", "version": [1, 0, 0] }
  ]
}
```

## Documentación de referencia

- Manifest: <https://learn.microsoft.com/en-us/minecraft/creator/reference/content/addonsreference/packmanifest>
- Versión a la que apuntar: <https://learn.microsoft.com/en-us/minecraft/creator/documents/practices/latestplatformversion>
- Guía comunitaria, más llevadera: <https://wiki.bedrock.dev/>
