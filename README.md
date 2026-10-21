# Entrega — Sesión 5: Git y GitHub

**Integrantes:** Emmanuel Franco Lopez y Manuel Galeano Alarcon  
**Proyecto:** Sistema de Riego Inteligente Automatizado con Python y Raspberry Pi Pico  
**Estado:** propuesta preliminar; componentes no comprados y pruebas físicas pendientes.


## Nombre del repositorio
`riego-inteligente-python-pico`

## Problema, objetivo y alcance del MVP
El riego manual puede ser irregular. El objetivo es diseñar un prototipo que lea humedad y controle el riego con bloqueo por depósito vacío. El MVP incluye lógica de control, futura conexión a Raspberry Pi Pico con MicroPython y una aplicación Python de escritorio. El montaje y la calibración están pendientes.

## Estructura propuesta
```text
README.md
docs/
src/
tests/
evidencias/
```

## Acuerdo de colaboración
Roles propuestos, confirmar entre los dos:
- Emmanuel Franco Lopez: documentación y revisión.
- Manuel Galeano Alarcon: integración de código y mantenimiento del repositorio.
Ambos revisarán cambios y registrarán únicamente pruebas reales.

## Primer commit sugerido
```bash
git init
git add README.md docs src tests
git commit -m "Agrega estructura inicial y especificación del proyecto"
```
Estos son comandos sugeridos; no prueban que se haya creado un commit. Después de crear el repositorio remoto, agregar la URL real y hacer `git push`.

## Cambio controlado y revisión por pares
Crear una rama, modificar una parte pequeña de la especificación, revisar con `git diff`, ejecutar pruebas pertinentes, crear un commit y abrir un pull request para que el compañero revise. Agregar el enlace real del PR y la observación cuando se haya hecho.

## Evidencia del cambio revisado
Pendiente de completar con hash real del commit, fecha, autor, revisor, comentario y enlace.
