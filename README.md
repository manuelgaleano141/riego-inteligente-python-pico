# Sistema de Riego Inteligente

**Integrantes:** Emmanuel Franco Lopez y Manuel Galeano Alarcon

## Descripción del proyecto

El proyecto busca desarrollar un sistema de riego inteligente que permita controlar el riego de una planta según la humedad del suelo y la disponibilidad de agua en el depósito.

La idea es utilizar una Raspberry Pi Pico RP2040 con MicroPython para controlar los sensores y la bomba de agua, además de un programa en Python para visualizar información desde el computador.

## Objetivo

Automatizar el riego de una planta y evitar que la bomba funcione cuando no haya suficiente agua en el depósito.

## Alcance actual

Por ahora, el proyecto se encuentra en etapa de desarrollo. Se ha trabajado en la lógica de control en Python y se han ejecutado pruebas automatizadas. Todavía falta comprar los componentes, realizar el montaje y comprobar el funcionamiento físico del sistema.

## Archivos del proyecto

- `control.py`: lógica de control del riego.
- `test_control.py`: pruebas automatizadas del programa.
- `especificacion_v1.md`: requisitos y funcionamiento esperado.
- `prompt_tecnico_v1.md`: instrucciones técnicas para desarrollar el proyecto.
- `problemas_ambiguedades.md`: dudas y aspectos pendientes de definir.
- `registro_uso_IA.md`: registro del uso de inteligencia artificial.
- `registro_debugging.md`: registro de pruebas y depuración.
- `acuerdo_equipo.md`: acuerdo de colaboración del equipo.
- `evidencias/`: evidencias de las pruebas realizadas.

## Estado del proyecto

Las pruebas de software realizadas hasta el momento han finalizado correctamente. La integración con la Raspberry Pi Pico, los sensores y la bomba de agua está pendiente.

## Trabajo pendiente

- Definir y calibrar el umbral de humedad con el sensor real.
- Verificar el funcionamiento del sensor de nivel de agua.
- Montar y probar el circuito de control de la bomba.
- Implementar y comprobar la comunicación entre la placa y el computador.
- Documentar las pruebas físicas cuando se realicen.
## Revisión del proyecto

La documentación y las pruebas de software se actualizarán a medida que avance el desarrollo.
