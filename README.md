# Entrega — Sesión 3: Prompt Engineering

**Integrantes:** Emmanuel Franco Lopez y Manuel Galeano Alarcon  
**Proyecto:** Sistema de Riego Inteligente Automatizado con Python y Raspberry Pi Pico  
**Estado:** propuesta preliminar; componentes no comprados y pruebas físicas pendientes.


## Entregables
1. MVP corregido.
2. Especificación v1.
3. Prompt técnico v1.
4. Código preliminar de lógica.
5. Ocho o más casos de prueba propuestos.
6. Registro de uso de IA (plantilla para completar con consultas reales).
7. Problemas y ambigüedades identificados.

## MVP
Leer humedad del suelo, decidir si se requiere riego, bloquear la bomba si el depósito está vacío y permitir supervisión desde una aplicación de PC. Se propone Raspberry Pi Pico RP2040 con MicroPython; no Arduino.

## Especificación v1
- **Entradas:** humedad ADC, estado del nivel del depósito, modo manual/automático.
- **Salidas:** decisión de activar bomba, estado por serial y registro local propuesto.
- **Reglas:** bloquear si el tanque está vacío; rechazar valores inválidos; limitar duración y aplicar pausa.
- **Restricciones:** sensor y componentes por elegir; calibración y conexiones pendientes; la bomba nunca debe conectarse directamente a un GPIO.
- **Criterio de aceptación:** las decisiones de software cumplen las reglas y luego se validan en hardware real.

## Prompt técnico v1
> Actúa como ingeniero de software y sistemas embebidos. Propón una solución modular de riego inteligente con Raspberry Pi Pico RP2040 y MicroPython, sin Arduino. Debe leer un sensor capacitivo por ADC, leer un interruptor de nivel y recibir comandos de una aplicación Python por USB serial. Antes de escribir código, detecta ambigüedades, riesgos eléctricos y preguntas sin resolver. Después propone lógica y pruebas. Bloquea la bomba si el depósito está vacío, valida entradas y limita el tiempo de riego. No afirmes pruebas que no se hayan realizado y marca los parámetros sin calibrar.

## Ambigüedades
- Umbrales ADC reales para suelo seco/húmedo.
- Polaridad del interruptor de nivel.
- Tensión, corriente de arranque y fuente de la bomba.
- MOSFET apto para control a 3,3 V.
- Comportamiento ante pérdida de comunicación.
- Duración de riego segura para la planta.

## Pruebas propuestas (pendientes de ejecutar)
| ID | Caso | Resultado esperado |
|---|---|---|
| 1 | Suelo seco y tanque lleno | Solicita riego |
| 2 | Suelo húmedo | No riega |
| 3 | Tanque vacío | Bomba bloqueada |
| 4 | Lectura ADC fuera de rango | Rechazo seguro |
| 5 | Tiempo máximo alcanzado | Bomba apagada |
| 6 | Durante pausa | No inicia otro pulso |
| 7 | Modo manual con tanque vacío | Bloqueo |
| 8 | Comando desconocido | Error controlado |

## Registro de uso de IA
Completar con la fecha, la consulta real, resumen de respuesta, decisión del equipo y verificación. No se simula una conversación como si hubiera ocurrido.

## Código de referencia
La lógica preliminar se incluye en `control.py`. No representa firmware probado en la Pico.
