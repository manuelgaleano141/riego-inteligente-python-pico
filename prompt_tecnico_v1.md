# Prompt técnico v1 — Sistema de riego inteligente

## 1. Contexto del proyecto

Estamos desarrollando un sistema de riego inteligente utilizando Python y una Raspberry Pi Pico RP2040. El objetivo es automatizar el riego de una planta según la humedad del suelo y la disponibilidad de agua en el depósito.

## 2. Objetivo

Crear un programa que permita controlar cuándo se debe activar o apagar una bomba de agua, teniendo en cuenta las lecturas del sensor de humedad y el nivel de agua disponible.

## 3. Entradas del sistema

- Lectura de humedad del suelo.
- Estado del sensor de nivel de agua del depósito.
- Modo de funcionamiento: automático o manual.
- Umbral de humedad definido para activar el riego.

## 4. Reglas de funcionamiento

- En modo automático, el sistema debe activar el riego cuando la humedad del suelo indique que la planta necesita agua.
- Si el depósito está vacío o el sensor indica un nivel bajo de agua, la bomba debe permanecer apagada.
- Si la lectura de humedad no es válida, el sistema no debe activar la bomba.
- En modo manual, el usuario podrá solicitar el riego, siempre que haya agua disponible.
- El sistema debe mostrar información que permita conocer la decisión tomada.

## 5. Salidas esperadas

- Estado de la bomba: encendida o apagada.
- Mensaje indicando la razón de la decisión.
- Información sobre posibles errores en las lecturas.

## 6. Restricciones técnicas

- El programa debe desarrollarse en Python.
- La Raspberry Pi Pico utilizará MicroPython para el control del hardware.
- La comunicación con el computador se realizará mediante USB serial.
- La bomba debe manejarse mediante un circuito de potencia adecuado, no directamente desde un pin de la Raspberry Pi Pico.
- Se debe comprobar que los voltajes de los sensores sean compatibles con la placa.

## 7. Pruebas que se deben realizar

- Comprobar el comportamiento cuando el suelo está seco.
- Comprobar el comportamiento cuando el suelo tiene suficiente humedad.
- Verificar que la bomba permanezca apagada cuando no haya agua.
- Probar entradas inválidas.
- Comprobar el funcionamiento de los modos automático y manual.
- Verificar que los errores no provoquen la activación inesperada de la bomba.

## 8. Indicaciones para generar el código

Antes de generar el código, revisa si hay requisitos ambiguos o información faltante. Señala los problemas encontrados y propón cómo aclararlos.

Después, desarrolla el código por partes, explica brevemente su funcionamiento y prepara pruebas para verificar las reglas establecidas. No afirmes que el hardware funciona si solamente se han realizado pruebas en Python.

## 9. Estado actual

Se han realizado pruebas automatizadas de la lógica de Python. La conexión y las pruebas físicas con la Raspberry Pi Pico, los sensores y la bomba están pendientes.
