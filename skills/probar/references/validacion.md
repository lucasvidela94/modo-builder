# Qué revisa el script

Material de consulta de `probar`. `scripts/revisar.py` cubre la primera lista; la segunda es para
cuando el juego rechaza un add-on que el script dio por bueno.

## Lo que el script verifica

- **Sintaxis**: cada `.json` de `addon/` parsea, con la línea y la columna del error.
- **Manifest**: `format_version` 2, `min_engine_version` presente, y los cuatro UUID bien formados y
  distintos entre sí.
- **Enlace entre packs**: el behavior pack declara en `dependencies` el UUID del header del resource
  pack. Sin eso los visuales no se ven.
- **Identificadores**: empiezan con el `namespace` de `config.json` y van en minúsculas.
- **Texturas**: cada nombre corto del índice tiene su PNG en la ruta declarada, y la ruta no lleva
  `textures/` ni `.png` (el índice los agrega solo).
- **Nombres visibles**: cada identificador del add-on tiene su línea en el `.lang`, con `item.` sin
  `.name` y `tile.` con `.name`.

## Cuando el add-on no carga y el script no encuentra nada

En orden, de lo más común a lo menos:

1. **El pack no aparece en la lista del mundo.** El `.mcaddon` no se importó: se abre con doble clic
   y Minecraft lo instala; después hay que activarlo en el mundo, en los packs de comportamiento y de
   recursos.
2. **El item no está en el inventario creativo.** Falta `menu_category` en la `description`, o el
   `components` quedó afuera (tiene que estar, aunque sea `{}`).
3. **Aparece con el nombre raro** (`item.miaddon:rayo_espada` en vez de "Espada de rayo"). El `.lang`
   tiene una clave distinta a la del identificador, o `languages.json` no lista `es_ES`.
4. **La textura es un cuadro violeta y negro.** El nombre corto del `minecraft:icon` no coincide con
   la clave de `item_texture.json`, o el archivo apunta a una ruta que no existe.
5. **El bloque se rompe al instante o es indestructible.** Ajustar
   `minecraft:destructible_by_mining`.
6. **El script no hace nada.** Casi siempre el manifest: falta el módulo `script`, el `entry` está
   mal, o la versión de `@minecraft/server` no existe en ese juego. Los errores de script salen en el
   registro del juego: en un mundo con "Contenido de creación" activado, o en
   `%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\logs` en Windows.
7. **Andaba y dejó de andar después de cambiar archivos.** El juego cachea los packs: cerrarlo y
   volver a abrirlo, y si sigue igual, quitar y volver a agregar el pack en el mundo.

## Validación oficial

Microsoft publica un validador con reglas para manifest, `min_engine_version`, items y bloques:
<https://learn.microsoft.com/en-us/minecraft/creator/reference/content/mctoolsvalreference/>. Cuando
un add-on da un error que el script no explica, esa es la fuente siguiente: cada regla dice qué
verifica, la severidad y cómo arreglarlo.

El editor oficial (Creator Tools) está en <https://github.com/Mojang/minecraft-creator-tools> y sirve
para editar visualmente, pero no hace falta para nada de este flujo.
