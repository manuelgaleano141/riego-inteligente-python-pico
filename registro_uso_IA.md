# Registro de uso de IA — Sesión 3

## Objetivo

Documentar el uso de herramientas de inteligencia artificial como apoyo para diseñar, desarrollar y verificar el sistema de riego inteligente.

## Consulta 1: Diseño de la lógica de control

**Pregunta realizada:** ¿Cómo estructurar la lógica de control del riego con Python?

**Resumen de la respuesta:** Se propuso una función para evaluar la humedad del suelo, el nivel de agua disponible y el modo de funcionamiento.

**Decisión del equipo:** Utilizar la propuesta como base para el módulo `control.py`, revisando su lógica antes de aceptarla.

**Verificación:** Se ejecutaron las pruebas automatizadas de `test_control.py`. Las ocho pruebas finalizaron correctamente con el resultado `OK`.

## Consulta 2: Manejo de entradas inválidas

**Pregunta realizada:** ¿Cómo comprobar el comportamiento del programa ante una lectura de humedad no numérica?

**Resumen de la respuesta:** Se propuso probar la función con una entrada de texto inválida y observar su respuesta.

**Decisión del equipo:** Ejecutar una prueba controlada desde la terminal de Python.

**Verificación:** La función devolvió `Decision(pump_on=False, reason='humedad_invalida')`, sin generar una excepción.tr

## Consulta 3: Documentación de pruebas

**Pregunta realizada:** ¿Cómo registrar los resultados de las pruebas en GitH

**Resumen de la respuesta:** Se recomendó documentar el comando ejecutado, el resultado observado y las limitaciones de las pruebas.

**Decisión del equipo:** Crear el archivo `evidencias/pruebas_python.txt`.

**Verificación:** Se comprobó que el archivo aparece en el repositorio de GitHub.

## Limitaciones y observaciones

La inteligencia artificial se utilizó como apoyo para el desarrollo y la documentación. Las respuestas se contrastaron mediante pruebas de software cuando fue posible.
Las pruebas realizadas validan la lógica de Python, pero no demuestran el funcionamiento físico de la Raspberry Pi Pico, el sensor de humedad ni la bomba. La integración y las pruebas del hardware siguen pendientes.
