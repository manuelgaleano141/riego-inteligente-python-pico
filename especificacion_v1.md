# Especificación v1 — Sistema de Riego Inteligente Automatizado

## 1. Información del proyecto

**Proyecto:** Sistema de Riego Inteligente Automatizado con Python y Raspberry Pi Pico  
**Asignatura:** Electiva Tecnológica 2  
**Integrantes:** Emmanuel Franco Lopez y Manuel Galeano Alarcon  
**Versión:** 1.0  
**Estado:** Diseño preliminar; pendiente de implementación y validación física.

## 2. Problema

El riego manual puede provocar un uso ineficiente del agua cuando no se tiene en cuenta la humedad del suelo. Se propone desarrollar un sistema que mida la humedad y controle una bomba de agua según condiciones configurables.

## 3. Objetivo general

Diseñar un sistema de riego automatizado que utilice una Raspberry Pi Pico, MicroPython y una aplicación desarrollada en Python para monitorear la humedad del suelo y controlar el riego.

## 4. Alcance del producto mínimo viable (MVP)

La primera versión deberá:

- Leer el valor de un sensor capacitivo de humedad.
- Permitir configurar un umbral de humedad.
- Activar o desactivar la bomba según la lectura y las reglas de control.
- Detectar el nivel bajo del depósito mediante un interruptor de flotador.
- Comunicar las lecturas y el estado del sistema con una aplicación de Python mediante comunicación serial USB.
- Mostrar mensajes de error cuando las lecturas o la comunicación no sean válidas.

La interfaz, el sensor y la bomba se encuentran pendientes de integración y pruebas físicas.

## 5. Componentes previstos

- Raspberry Pi Pico con microcontrolador RP2040.
- Sensor capacitivo de humedad del suelo.
- Interruptor de flotador para detectar nivel bajo de agua.
- MOSFET compatible con la señal de control para conmutar la bomba.
- Bomba de agua de corriente continua con alimentación apropiada.
- Fuente de alimentación para la bomba.
- Cable USB para comunicación y programación.
- Cables y elementos de conexión.

## 6. Entradas

- Lectura analógica del sensor de humedad.
- Estado del interruptor de flotador.
- Umbral de humedad configurado por el usuario.
- Comandos de consulta o configuración enviados desde la aplicación.

## 7. Salidas

- Estado de la bomba: encendida o apagada.
- Lecturas de humedad.
- Estado del nivel de agua.
- Mensajes de funcionamiento y errores.
- Información enviada a la aplicación mediante comunicación serial.

## 8. Reglas de funcionamiento

1. El sistema debe adquirir y validar las lecturas del sensor.
2. Si la humedad indica que el suelo está seco y hay agua disponible, podrá activar el riego.
3. Si se alcanza el nivel de humedad objetivo, debe detener el riego.
4. Si se detecta nivel bajo de agua, la bomba debe permanecer apagada.
5. Ante lecturas inválidas o pérdida de comunicación, el sistema debe adoptar un estado seguro y evitar activaciones no justificadas.
6. El umbral y la interpretación de las lecturas deben ajustarse mediante calibración del sensor.

## 9. Restricciones técnicas y de seguridad

- El firmware de la Raspberry Pi Pico se desarrollará en MicroPython, no en Arduino.
- La aplicación de escritorio se desarrollará en Python.
- Los pines GPIO de la Pico trabajan con lógica de 3,3 V y no deben recibir señales superiores a ese nivel.
- La bomba no debe conectarse directamente a un GPIO.
- La bomba utilizará una etapa de potencia adecuada y una alimentación compatible con sus especificaciones.
- Antes de montar el circuito, se verificarán las conexiones, la corriente de la bomba y la compatibilidad del MOSFET.
- No se afirmará que el hardware funciona hasta realizar pruebas físicas.

## 10. Pruebas previstas

- Verificar la lectura del sensor en condiciones secas y húmedas.
- Comprobar la respuesta al umbral de humedad.
- Comprobar que la bomba no se active cuando el depósito indique nivel bajo.
- Verificar la comunicación serial entre la Pico y la aplicación.
- Comprobar el comportamiento ante lecturas inválidas y desconexiones.
- Validar el encendido y apagado de la bomba una vez construido el circuito.

## 11. Criterios de aceptación

El MVP se considerará validado cuando:

- Las lecturas del sensor sean interpretadas correctamente.
- La lógica de control responda al umbral de humedad configurado.
- La bomba permanezca apagada cuando el depósito indique un nivel bajo de agua.
- La aplicación y la Raspberry Pi Pico puedan intercambiar información mediante comunicación serial USB.
- Los errores de lectura y comunicación se manejen de forma segura.
- Las pruebas de funcionamiento se documenten con sus resultados reales.

**Estado actual:** las pruebas automatizadas de la lógica de Python se han ejecutado correctamente. La integración con la Raspberry Pi Pico, el sensor, el interruptor de flotador y la bomba sigue pendiente de implementación y validación física.
## 12. Estado actual y pendientes

Esta especificación describe el diseño propuesto. La compra de componentes, el montaje del circuito, la calibración y las pruebas físicas están pendientes. Los resultados se documentarán cuando se ejecuten realmente.

## 13. Cambios de versión

**Versión 1.0:** definición inicial del problema, alcance, componentes, reglas, restricciones y pruebas previstas.
