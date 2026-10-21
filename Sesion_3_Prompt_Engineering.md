# Sesión 3 — Prompt Engineering con IA
**Integrantes:** Emmanuel Franco Lopez y Manuel Galeano Alarcon  
**Estado:** propuesta; pruebas planificadas, no reportadas como ejecutadas.

## MVP corregido
Lectura de humedad, decisión de riego, bloqueo por depósito vacío, control manual/automático y supervisión desde PC.

## Especificación v1
Ver [`especificacion_v1.md`](especificacion_v1.md).

## Prompt técnico v1
> Actúa como ingeniero de software y sistemas embebidos. Diseña una propuesta modular para riego inteligente con Raspberry Pi Pico RP2040 y MicroPython, sin Arduino. Entradas: ADC de sensor capacitivo, interruptor de nivel y comandos seriales desde una aplicación Python. Bloquea la bomba si el depósito está vacío, limita duración y pausa, valida entradas y no asumas calibración. Antes de escribir código, enumera ambigüedades, riesgos eléctricos y preguntas necesarias. Después propone módulos y pruebas. No afirmes que código o hardware se han probado sin evidencia.

## Ambigüedades identificadas
- Valores ADC para suelo seco/húmedo: requiere calibración.
- Polaridad del interruptor de nivel: confirmar con componente real.
- Tensión/corriente de bomba y MOSFET: pendiente de selección.
- Comportamiento ante pérdida de USB: definir.
- Duración máxima segura: definir según planta y recipiente.
- Ruido de sensor y posible histéresis: evaluar con lecturas reales.

## Ocho pruebas mínimas propuestas
| ID | Escenario | Resultado esperado | Estado |
|---|---|---|---|
| P01 | Suelo seco, tanque lleno | Solicita riego | Pendiente |
| P02 | Suelo húmedo | No riega | Pendiente |
| P03 | Tanque vacío | Bloquea bomba | Pendiente |
| P04 | Lectura fuera de rango | Rechaza lectura | Pendiente |
| P05 | Duración máxima alcanzada | Apaga bomba | Pendiente |
| P06 | Durante pausa | No inicia otro pulso | Pendiente |
| P07 | Manual con tanque vacío | Bloquea comando | Pendiente |
| P08 | Comando desconocido | Error controlado | Pendiente |

## Registro de uso de IA
Completar con consultas reales: fecha, prompt, respuesta resumida, decisión del equipo y verificación. No se presenta una conversación inventada como historial real.

## Problemas/ambigüedades
La calibración, la polaridad del sensor de nivel, el dimensionamiento de fuente/MOSFET y la comunicación serial deben verificarse antes del montaje.
