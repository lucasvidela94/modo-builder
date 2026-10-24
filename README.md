# Modo Builder

Skills para que un agente de código arme **add-ons de Minecraft Bedrock** a partir de ideas en
lenguaje común. La persona describe lo que imagina; el agente escribe los JSON, las texturas y el
paquete final.

Pensado para alguien que **no programa**: no hay que tocar archivos ni ejecutar comandos.

```bash
npx skills add lucasvidela94/modo-builder
```

## Qué trae

Siete skills, cada una un oficio del proceso:

- **idea-a-plan** — convierte una idea vaga en un plan corto y confirmado (`plan.md`).
- **addon-base** — arma la estructura del add-on con los dos manifest y sus UUID.
- **item-bloque-mob** — escribe los JSON de items, bloques y mobs.
- **texturas-y-modelos** — genera las texturas PNG y los modelos.
- **probar** — valida todo, empaqueta el `.mcaddon` y traduce los errores.
- **guardar-version** — puntos de restauración con git, para probar sin miedo.
- **scripts-avanzados** — efectos y lógica con la Script API, cuando el JSON no alcanza.

El flujo completo: **idea → plan → prototipo → probar → ajustar → guardar versión**.

## Cómo se usa

1. Creá una carpeta para el proyecto (por ejemplo `C:\proyectos\mi-addon`) y abrila como proyecto en
   tu agente de código (opencode, Claude Code, Codex).
2. Instalá las skills ahí adentro:

   ```bash
   npx skills add lucasvidela94/modo-builder
   ```

3. Copiá `templates/AGENTS.md` a la raíz del proyecto (son las reglas de trato y de trabajo del
   agente) y `templates/opencode.json` si usás opencode.
4. Pedile lo que querés, en tus palabras: *"quiero un item que lance rayos"*.

El agente va a preguntar de a una cosa, mostrar el plan, crear el prototipo mínimo y dejar el
`.mcaddon` en `dist/` para que lo abras con doble clic.

## Requisitos

- **Node.js** (para `npx skills` y, más adelante, para compilar scripts).
- **Git** (para los puntos de restauración).
- **Minecraft Bedrock Edition** — no sirve Java. Los add-ons de una edición no funcionan en la otra.
- Python 3 con Pillow, sólo si querés que el agente dibuje las texturas placeholder.

## Versión del juego

Las skills apuntan a **Bedrock 1.26.x** (retail 1.26.52, septiembre 2026) y usan
`format_version` **1.26.50** en las definiciones, `manifest` **format_version 2** y
`@minecraft/server` **2.9.0** en la Script API.

Fijá una versión al empezar el proyecto y no la cambies a mitad: el agente guarda la elegida en
`addon/config.json` y la lee de ahí. Los detalles y cómo actualizarlos están en
[`skills/addon-base/references/manifest.md`](skills/addon-base/references/manifest.md).

## Estructura del repo

```
skills/<nombre>/SKILL.md      cada oficio (el CLI instala el directorio entero)
skills/<nombre>/references/   material de consulta, se lee sólo cuando hace falta
templates/                    archivos para copiar al proyecto nuevo
```

## Compatibilidad

Las skills siguen el formato abierto de [Agent Skills](https://skills.sh) (`SKILL.md` con
frontmatter `name` + `description`), así que funcionan en opencode, Claude Code, Codex y cualquier
agente que lea ese formato. Los `description` están en inglés para que el agente las encuentre: el
contenido está en castellano.

## Licencia

MIT — ver [LICENSE](LICENSE). Minecraft es una marca de Mojang Studios; este proyecto no está
afiliado ni respaldado por ellos.
