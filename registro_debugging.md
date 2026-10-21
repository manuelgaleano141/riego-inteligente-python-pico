# Registro de debugging — Sistema de Riego Inteligente

## 1. Información de la prueba

- **Proyecto:** Sistema de Riego Inteligente Automatizado con Python y Raspberry Pi Pico.
- **Archivo evaluado:** `control.py`.
- **Pruebas automatizadas:** `test_control.py`.
- **Entorno:** Python en Windows.
- **Estado del hardware:** No montado; validación física pendiente.

## 2. Problema encontrado

Al agregar nuevas pruebas, se detectó que la función `decide_watering()` aceptaba el valor booleano `True` como si fuera un umbral de humedad válido.

La prueba `test_boolean_threshold` esperaba que la función devolviera `umbral_invalido`, pero inicialmente devolvió `humedad_suficiente`.

## 3. Hipótesis

El problema estaba en la validación de `threshold_percent`, porque Python permite tratar valores booleanos como números enteros. Por esta razón, era necesario comprobar explícitamente que el umbral no fuera de tipo `bool`.

## 4. Prueba realizada

Se ejecutaron las pruebas automatizadas con el comando:

`py -m unittest -v test_control.py`

En la primera ejecución de las 12 pruebas, 11 pasaron y `test_boolean_threshold` falló. El resultado permitió identificar el problema de validación.

También se ejecutó el siguiente comando para comprobar directamente el comportamiento de la función:

`py -c "from control import decide_watering; print(decide_watering(20, True, threshold_percent=True))"`

Después de la corrección, el resultado observado fue:

`Decision(pump_on=False, reason='umbral_invalido')`

## 5. Corrección aplicada

Se modificó la validación del umbral para rechazar valores que no sean numéricos, valores booleanos y valores fuera del rango de 0 a 100.

La corrección se verificó ejecutando nuevamente las pruebas automatizadas.

## 6. Pruebas de regresión y resultado final

Después de aplicar la corrección, se ejecutó nuevamente:

`py -m unittest -v test_control.py`

**Resultado observado:**
- 12 pruebas ejecutadas.
- Las 12 pruebas finalizaron con `ok`.
- Resultado final: `OK`.

La captura de la terminal se conserva como evidencia de esta ejecución.

Las pruebas cubrieron suelo seco, suelo húmedo, depósito vacío en modo automático y manual, modo inválido, lecturas inválidas, tipo de dato incorrecto, solicitud manual, humedad negativa y umbrales inválidos, incluido el caso booleano.

## 7. Prueba controlada de entrada inválida

- **Objetivo:** comprobar cómo responde la función ante una lectura de humedad no numérica.
- **Función evaluada:** `decide_watering()`.
- **Entrada utilizada:** `'invalido'`, con `tank_has_water=True`.
- **Comando ejecutado:** `py -c "from control import decide_watering; print(decide_watering('invalido', True))"`
- **Resultado observado:** `Decision(pump_on=False, reason='humedad_invalida')`.
- **Interpretación:** la función rechazó la lectura inválida, mantuvo la bomba apagada y devolvió una razón descriptiva sin generar una excepción.

## 8. Uso de inteligencia artificial

Se utilizó ChatGPT como apoyo para interpretar el fallo de una prueba, revisar la validación del umbral y proponer una corrección. La solución se comprobó ejecutando nuevamente las pruebas automatizadas en Python.

## 9. Limitaciones y trabajo pendiente

Las pruebas realizadas validan la lógica del programa en Python. No demuestran el funcionamiento físico de la Raspberry Pi Pico, los sensores ni la bomba de agua.

Quedan pendientes el montaje del hardware, la integración con MicroPython, las pruebas físicas y la verificación de la comunicación entre la placa y el computador.

## 10. Conclusión

Se identificó y corrigió un error en la validación del umbral de humedad. Después de la corrección, las 12 pruebas automatizadas finalizaron correctamente. La evidencia corresponde a pruebas de software realizadas en Windows y no a una validación física del sistema.
