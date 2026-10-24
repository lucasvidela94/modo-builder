---
name: guardar-version
description: Save and restore restore-points of the project with git, named in words the person understands, and undo the last change. Use when the person says guardá el punto, volvé atrás or mostrame las versiones, and before any big change.
---

# Guardar versión

**Criterio de cierre:** existe un commit que la persona puede nombrar por su descripción, o el
proyecto quedó igual que en el punto que eligió. Los dos casos terminan con una frase que la persona
entiende, sin hashes en pantalla.

## Guardar un punto

1. Verificá que haya git (`git status`). Si el proyecto no está iniciado, corré `git init` una vez y
   creá un `.gitignore` con `dist/` y `node_modules/`. La carpeta `addon/` sí se versiona: es el
   proyecto. Lo que no se guarda es el empaquetado.
2. Pedí un nombre corto en palabras simples ("espada de rayo funcionando"). Si no quiere pensar,
   usá la fecha y hora.
3. Guardá:

   ```
   git add -A
   git commit -m "Punto: NOMBRE"
   ```

4. Confirmá en una frase: "Guardé el punto 'espada de rayo funcionando'. Si algo sale mal, volvemos
   acá."

## Volver atrás

1. Listá los últimos puntos y mostrá **las descripciones, sin hashes**:
   ```
   git log --oneline -10
   ```
2. Preguntá a cuál quiere volver.
3. Guardá primero lo que tiene ahora como un punto nuevo, así nada se pierde.
4. Restaurá el contenido de ese punto sin borrar la historia:
   ```
   git checkout <hash> -- addon
   ```
   Avisá antes de correrlo y confirmá el resultado abriendo el juego: el punto está restaurado
   cuando el contenido volvió a andar, no cuando el comando terminó.

## Reglas

- Un punto por idea terminada: antes de un cambio grande, y cuando algo pasa a andar en el juego.
- Si git no está instalado, contale que hace falta y dale el comando de instalación
  (`winget install Git.Git` en Windows) para que lo corra. Vos corrés los comandos del proyecto; no
  le pidas a la persona que ejecute los tuyos.
