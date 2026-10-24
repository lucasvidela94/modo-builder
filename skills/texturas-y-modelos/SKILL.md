---
name: texturas-y-modelos
description: Create the PNG textures and geometry models of a Bedrock add-on with the size, name and path Minecraft expects, and register them in the index. Use when an item, block or mob needs its own image or shape.
---

# Texturas y modelos

**Criterio de cierre:** cada textura que el JSON nombra existe como PNG, con el tamaño y el nombre
correctos, en la ruta que el índice declara. Y se ve **en el juego**, no sólo en el explorador de
archivos.

## Texturas

- PNG con fondo transparente para items; 16×16 píxeles como base. 32×32 y 64×64 también sirven.
- Nombre en minúsculas, sin tildes ni espacios: `rayo_espada.png`.
- Rutas: items en `resource_packs/mi_addon_rp/textures/items/`, bloques en `textures/blocks/`.
- Después de agregarla, registrala en el índice: `item_texture.json` para items,
  `terrain_texture.json` para bloques.

### Dibujar un placeholder

Cuando la persona todavía no tiene el dibujo, generá uno simple con Python y Pillow:

```
python3 -m pip install pillow     # en Windows: py -m pip install pillow
```

Creá el PNG de 16×16 con los colores acordados y decile que es un **placeholder**: puede reemplazarlo
por un dibujo propio cuando quiera (Aseprite, GIMP, Krita o Paint.NET, todos abren un PNG de 16×16).

## Modelos

- Los modelos son `.geo.json`: `resource_packs/mi_addon_rp/models/entity/` para mobs,
  `models/blocks/` para bloques.
- Un modelo simple sale de un **molde**: copiá el de vanilla parecido y cambiá nombre y texturas.
- Para algo con forma propia, el camino corto es Blockbench (gratis), que exporta directo al formato
  Bedrock. Contale los pasos en tres líneas y que después vuelve a pedirte que lo conecte.

## Revisión

Antes de dar una textura por buena:

1. El PNG abre (no está corrupto ni es un archivo con la extensión cambiada).
2. El nombre y la ruta coinciden con lo que dice el JSON del item o del bloque.
3. La entrada del índice apunta a esa ruta.

Cuando algo no coincide, corregilo y contale a la persona en una frase qué pasaba. Si la textura no
aparece en el juego pero los tres puntos de arriba están bien, el problema está en el nombre corto
del índice o en el caché del juego: cerralo y volvé a abrirlo antes de tocar nada más.
