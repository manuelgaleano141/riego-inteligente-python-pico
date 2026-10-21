# Entrega — Sesión 4: Debugging con IA

**Integrantes:** Emmanuel Franco Lopez y Manuel Galeano Alarcon  
**Proyecto:** Sistema de Riego Inteligente Automatizado con Python y Raspberry Pi Pico  
**Estado:** propuesta preliminar; componentes no comprados y pruebas físicas pendientes.


## 1. Módulo ejecutable
El archivo `control.py` contiene una función de lógica que se puede ejecutar y probar sin hardware. Es una base de referencia, no un sistema físico validado.

## 2. Pruebas documentadas
Los casos están en `test_control.py`. Ejecutar desde esta carpeta:
```bash
python -m unittest -v test_control.py
```
Las pruebas deben ejecutarse en el equipo del grupo y guardar la salida real como evidencia.

## 3. Intento de ruptura propuesto
Solicitar riego manual con el depósito vacío y humedad baja. Resultado esperado: la decisión mantiene la bomba apagada. Marcar como pendiente hasta ejecutarlo.

## 4. Registro de debugging con IA
No se inventan fallos experimentales. Registrar cualquier fallo que realmente ocurra con el formato de `registro_debugging.md`.

## 5. Corrección, validación y regresión
Después de un cambio, ejecutar todas las pruebas y registrar salida anterior y posterior. La evidencia de lógica no valida sensores, bomba ni comunicación serial.

## 6. Defensa oral de dos minutos
“Somos Emmanuel Franco Lopez y Manuel Galeano Alarcon. Proponemos un sistema de riego con Raspberry Pi Pico y MicroPython. La lógica recibe la humedad, verifica el nivel del depósito y decide si permite regar. Hemos separado la lógica para poder probar casos de seguridad antes de montar el circuito. En esta etapa el hardware no se ha comprado ni probado físicamente, así que no confundimos los casos definidos con pruebas físicas realizadas. El siguiente paso es ejecutar las pruebas automatizadas, documentar fallos reales y validar los componentes y conexiones antes de afirmar que el prototipo funciona.”
