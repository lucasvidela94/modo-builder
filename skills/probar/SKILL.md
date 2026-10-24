---
name: probar
description: Validate every JSON and path of a Bedrock add-on, package the .mcaddon and translate errors into plain words. Use after each change, before telling the person anything is ready.
---

# Probar

**Criterio de cierre:** todo archivo JSON del add-on parsea, cada referencia entre archivos resuelve,
y el `.mcaddon` nuevo está en `dist/`. Sin esto corrido, nada está listo: "debería andar" no cuenta.

## Paso 1: que todo JSON parsee

```
python3 skills/probar/scripts/revisar.py
```

El script revisa la sintaxis de todos los `.json` de `addon/`, y después las referencias que el JSON
solo no ve: UUIDs repetidos, el UUID del resource pack declarado por el behavior pack, cada
identificador con el `namespace` de `config.json`, cada textura nombrada con su PNG y su entrada en
el índice, y cada clave del `.lang` apuntando a algo que existe.

Si encuentra algo, lo dice con archivo y motivo. Se arregla y se vuelve a correr.

## Paso 2: que cargue en el juego

Un add-on puede estar impecable y no cargar. Antes de decirlo listo, confirmá con la persona que el
`.mcaddon` abre en Minecraft y que el contenido aparece:

- El item o bloque se ve en el inventario creativo, en la categoría que dice el `menu_category`.
- El nombre que muestra es el del `.lang`, no el identificador crudo.
- El mob aparece cuando se invoca y se mueve.

## Paso 3: empaquetar

```
python3 skills/probar/scripts/empaquetar.py
```

Deja `dist/mi_addon.mcaddon` con `behavior_packs/` y `resource_packs/` en la raíz del zip. Si el
proyecto ya tenía otra forma de empaquetar, esa manda.

Cerrá Minecraft antes de reemplazar un `.mcaddon` que ya está abierto: Windows lo bloquea y el
empaquetado falla.

## Paso 4: contarle a la persona

- Si anda: "Listo, abrí `dist\mi_addon.mcaddon` con doble clic y probalo en un mundo nuevo."
- Si hay un error: qué archivo, qué pasaba y qué hiciste. Una o dos frases, sin jerga.

## Reglas

- Si el error viene de adentro de Minecraft y no sabés la causa, decí que no estás seguro y pedí el
  mensaje exacto o una captura. Inventar un diagnóstico hace perder tiempo.
- Los archivos de `dist/` que ya estaban se quedan, salvo que la persona pida limpiarlos.
