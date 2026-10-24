# Script API

Material de consulta de `scripts-avanzados`.

## Versiones

`@minecraft/server` es el módulo que se usa casi siempre. La versión se declara en `dependencies` del
behavior pack y tiene que existir en el juego instalado.

**Estables (no piden experimentos), verificadas en octubre de 2026:** `2.9.0` (la más nueva), `2.8.0`,
`2.7.0`, `2.6.0`, `2.5.0`, `2.4.0`, `2.3.0`, `2.2.0`, `2.1.0`, `2.0.0`, y la serie `1.x` de las
versiones viejas del juego.

**Beta (piden el experimento "Beta APIs"):** `2.10.0-beta` y anteriores. Cambian sin aviso.

Atajo: desde la 1.21.120 se puede poner `"version": "beta"` para tomar siempre la última beta. Sirve
para experimentar; para un proyecto que la persona va a usar, dejá la estable.

El otro módulo común es `@minecraft/server-ui` (formularios en pantalla), hoy `2.1.0` estable, y pide
`@minecraft/server@2.0.0` o superior.

## Eventos

El módulo expone `world.afterEvents` (después de que pasa) y `world.beforeEvents` (antes, y permite
cancelar). Los que más se usan al empezar:

- `itemUse` — alguien usa un item. Trae `itemStack` y `source`.
- `playerInteractWithBlock` — usa o toca un bloque.
- `entityHurt` — algo recibe daño. Trae la entidad y el daño.
- `entityDie` — algo muere.
- `playerSpawn` — alguien entra al mundo o reaparece.

En `beforeEvents`, tocar el mundo directamente da error: hay que diferir con `system.run(() => ...)`.

## Si usás TypeScript

Se puede escribir en `.ts` y compilar a `scripts/main.js`. Hace falta Node.js y `npm`. Antes de
instalar nada, contale a la persona qué se va a instalar y para qué; después de compilar, corré
`probar`.

Los tipos salen de `npm i -D @minecraft/server`, con la misma versión que declaraste en el manifest:
si divergen, el editor te deja escribir cosas que el juego rechaza.

## Documentación

- Índice oficial de la API: <https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/>
- `@minecraft/server`: <https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server>
- Versiones y estabilidad: <https://wiki.bedrock.dev/scripting/scripting-intro>
- Ejemplos concretos: <https://wiki.bedrock.dev/scripting/starting-scripts>
