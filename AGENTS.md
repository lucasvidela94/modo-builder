# Convenciones de este repo

Skill package para crear add-ons de Minecraft Bedrock. Las skills son el producto; el README es el
índice para humanos y el escaparate para `npx skills find`.

## Reglas de escritura

Escribimos para agentes. Antes de agregar o editar una skill, tené presente el resumen de
`writing-for-agents` que aplica acá:

- **El `description` es un puntero, no un resumen.** Qué es el material y las ramas que lo disparan
  (un trigger por rama, sin sinónimos). Va en inglés y con la palabra líder adelante: es lo único que
  se carga siempre.
- **Cuerpo en castellano**, imperativo, segunda persona, voseo. La persona que usa esto no programa:
  sin jerga sin traducir en la misma frase.
- **Criterio de cierre en cada skill**: qué tiene que ser cierto para darlo por terminado ("todo JSON
  parsea", "el efecto pasa en el juego"), no "quedó listo".
- **Positivo antes que prohibición**: describí lo que hay que hacer. Una prohibición sólo se queda
  como guardarraíl duro (borrar archivos, tocar fuera del proyecto).
- **Divulgación progresiva**: lo que sólo algunas ramas necesitan va en `references/`; lo ejecutable,
  en `scripts/`. El `SKILL.md` queda corto y atento.
- **Palabra líder** en vez de frases largas: *prototipo*, *plan*, *molde* (un archivo de vanilla
  copiado como base), *punto de restauración*, *anda en el juego* (la única prueba que vale).
- **Un solo lugar por significado**: si un dato vive en dos skills, dejalo en una y nombrala desde la
  otra.

## Verificación

Cada dato técnico (nombre de componente, versión, ruta) sale de la documentación oficial o de la
wiki, no de la memoria del modelo. Cuando cambie una versión de Bedrock, actualizá
`skills/addon-base/references/manifest.md`, `skills/item-bloque-mob/references/componentes.md` y el
README de una sola vez: son los tres lugares donde vive la versión.

## Antes de commitear

- `name` del frontmatter igual al nombre de la carpeta.
- Ningún `SKILL.md` en la raíz del repo: eso rompe el descubrimiento del CLI.
- Corré `npx skills add . --list` desde la raíz y confirmá que aparecen las ocho.
- Los scripts (`revisar.py`, `empaquetar.py`) andan sin dependencias externas: mantenelo así.
