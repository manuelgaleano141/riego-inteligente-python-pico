# Registro de uso de IA — Sesión 3

## Objetivo

Documentar el uso de herramientas de inteligencia artificial como apoyo para diseñar, desarrollar, probar y mejorar el sistema de riego inteligente.

## Consulta 1: Diseño de la lógica de control

**Pregunta realizada:** ¿Cómo estructurar la lógica de control del riego con Python?

**Resumen de la respuesta:** Se propuso una función para evaluar la humedad del suelo, el nivel de agua disponible y el modo de funcionamiento.

**Decisión del equipo:** Utilizar la propuesta como base para el módulo `control.py`, revisando su lógica antes de aceptarla.

**Verificación:** Se ejecutaron pruebas automatizadas para comprobar el comportamiento de la función.

## Consulta 2: Manejo de entradas inválidas

**Pregunta realizada:** ¿Cómo comprobar el comportamiento del programa ante una lectura de humedad no numérica?

**Resumen de la respuesta:** Se propuso probar la función con una entrada de texto inválida y observar su respuesta.

**Decisión del equipo:** Ejecutar una prueba controlada desde la terminal de Python.

**Verificación:** La función devolvió `Decision(pump_on=False, reason='humedad_invalida')`, sin generar una excepción.

## Consulta 3: Corrección de un error en el umbral

**Problema encontrado:** Una prueba mostró que el programa aceptaba `True` como umbral de humedad, aunque debía considerarlo inválido.

**Apoyo de la IA:** Se utilizó ChatGPT para revisar la validación y proponer una corrección que rechazara los valores booleanos.

**Decisión del equipo:** Modificar la condición de validación en `control.py`.

**Verificación:** Se ejecutó nuevamente `py -m unittest -v test_control.py`. Las 12 pruebas finalizaron correctamente con el resultado `OK`.

## Consulta 4: Documentación de las pruebas

**Pregunta realizada:** ¿Cómo registrar los resultados de las pruebas y las limitaciones del proyecto?

**Resumen de la respuesta:** Se recomendó documentar los comandos utilizados, los resultados observados, los errores encontrados y las correcciones realizadas.

**Decisión del equipo:** Registrar los resultados en `registro_debugging.md` y conservar la captura de la terminal como evidencia.

**Verificación:** Se comprobó en la terminal que las 12 pruebas automatizadas pasaron después de la corrección.

## Limitaciones y observaciones

La inteligencia artificial se utilizó como apoyo para el desarrollo, la depuración y la documentación. Las propuestas se comprobaron mediante pruebas de software cuando fue posible.

Las pruebas realizadas validan la lógica de Python, pero no demuestran el funcionamiento físico de la Raspberry Pi Pico, los sensores ni la bomba. La integración y las pruebas del hardware siguen pendientes.
