---
name: idea-a-plan
description: Turn a vague mod idea into a confirmed plan.md before any file exists. Use when the person describes a new item, block, mob or effect, or wants to change one already planned.
---

# Idea a plan

**Criterio de cierre:** existe una idea que la persona confirmó con sus palabras, y está escrita en
`plan.md`. Hasta entonces no se crea ningún archivo del add-on.

## Pasos

1. Escuchá la idea entera sin interrumpir. Todavía no toca mirar ni crear archivos.
2. Preguntá lo que falte, **de a una cosa por vez**, con opciones concretas entre las que elegir:
   - ¿Qué hace cuando la usás o la pisás?
   - ¿Cómo se consigue? (crafteo, tirando de un mob, comprándola, apareciendo en cofres)
   - ¿Cómo se ve? (color, material, forma, o una comparación: "como una espada de hielo")
   - ¿Es un item, un bloque o un mob?
3. Armá el plan con este formato y mostralo:

   ```
   Nombre: Espada de rayo
   Tipo: item
   Qué hace: al usarla, cae un rayo sobre el mob más cercano
   Cómo se consigue: receta con 2 barras de cobre y 1 palo
   Aspecto: hoja amarilla con chispas, mango marrón
   Necesita: 1 textura, 1 receta, 1 nombre en el idioma, y lógica (requiere scripts)
   ```

4. Pedí el visto bueno: "¿Así está bien, o cambiamos algo?"
5. Cuando confirme, escribí el plan en `plan.md`, en la raíz del proyecto. Si ya había un plan,
   agregá la idea nueva como una sección aparte debajo, con la fecha.

## Reglas

- Ante una idea grande, proponé el **prototipo** más chico que se pueda probar en el juego (el item
  sin el efecto, y el efecto después). Un prototipo que anda enseña más que un plan perfecto.
- Cuando la idea necesite eventos, contadores o efectos en el mundo, marcala en el plan como
  **requiere scripts** y avisá que eso viene en una segunda vuelta.
- Ofrecé sólo lo que la persona pidió. Si se te ocurre algo que suma, preguntá si lo quiere antes de
  sumarlo al plan.
