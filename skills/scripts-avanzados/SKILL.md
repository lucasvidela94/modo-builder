---
name: scripts-avanzados
description: Add real behaviour to a Bedrock add-on with the JavaScript Script API (@minecraft/server) for events, counters and world effects that JSON cannot do. Use when the plan is marked requiere scripts, after the base prototype works.
---

# Scripts avanzados

**Criterio de cierre:** el efecto pasa **en el juego**, no en la consola del script. El módulo está
en el manifest con su UUID propio, la versión de la API está anotada en `config.json`, y la persona
puede describir en una frase qué pasa cuando usa el objeto.

## Cuándo entra

- El plan dice **requiere scripts**, o la persona pide algo que el JSON no puede hacer: pasar cuando
  se usa un item, contar cosas, afectar el mundo, decidir según una condición.
- El prototipo sin efecto ya anda (item que aparece en el inventario, bloque que se coloca). Primero
  el objeto, después el comportamiento.

## Preparar el módulo

Agregá al `manifest.json` del behavior pack un módulo de scripts con **UUID nuevo**:

```json
{ "type": "script", "language": "javascript", "uuid": "UUID-MODULO-SCRIPT",
  "entry": "scripts/main.js", "version": [1, 0, 0] }
```

Y en `dependencies`, junto al UUID del resource pack:

```json
{ "module_name": "@minecraft/server", "version": "2.9.0" }
```

La versión sale de `config.json` → `script_api` (hoy **2.9.0**, la estable). Las versiones beta piden
el experimento "Beta APIs" encendido en el mundo y cambian sin aviso: usalas sólo si la persona lo
pide y entendiendo que puede romperse. Los detalles están en `references/script-api.md`.

## Escribir el código

`addon/behavior_packs/mi_addon_bp/scripts/main.js`, con un solo propósito por archivo:

```javascript
import { world } from "@minecraft/server";

world.afterEvents.itemUse.subscribe((event) => {
  if (event.itemStack?.typeId !== "miaddon:rayo_espada") return;
  event.source.sendMessage("¡Rayo!");
});
```

Ese ejemplo sólo manda un mensaje, y sirve para probar que el módulo carga. El efecto real se escribe
después, buscando el método exacto en la documentación de esa versión de la API: un nombre de método
inventado no falla al escribir, falla en el juego, que es donde más caro sale.

## Reglas

- Explicá el código en una o dos frases cuando lo entregues, sin leerlo en voz alta.
- Si el script no carga, revisá en este orden: UUID y `entry` del módulo en el manifest, la versión
  de la dependencia, y por último el código. El error suele estar en el manifest.
- Después de cada cambio acá, corré `probar` y pedí que se mire en el juego.
