# Registro de debugging — Sistema de Riego Inteligente

## 1. Información de la prueba

- **Proyecto:** Sistema de Riego Inteligente Automatizado con Python y Raspberry Pi Pico.
- **Archivo evaluado:** `control.py`.
- **Pruebas automatizadas:** `test_control.py`.
- **Fecha de ejecución:** 20 de octubre de 2026.
- **Entorno:** Python en Windows.
- **Estado del hardware:** No montado; validación física pendiente.

## 2. Evidencia disponible

Se ejecutó el siguiente comando en la terminal:

`py -m unittest -v test_control.py`

El resultado observado fue:

- Ocho pruebas ejecutadas.
- Las ocho pruebas finalizaron con `ok`.
- Resultado final: `OK`.

La captura de la terminal se conserva como evidencia visual de esta ejecución.

## 3. Casos comprobados

Las pruebas ejecutadas cubrieron los siguientes casos:

- Suelo seco.
- Suelo húmedo.
- Depósito vacío en modo automático.
- Depósito vacío en modo manual.
- Modo de funcionamiento inválido.
- Lectura inválida.
- Tipo de dato inválido.
- Solicitud de riego manual.

## 4. Resultado de la validación

Las pruebas automatizadas finalizaron correctamente en el entorno Python. Esto valida los casos contemplados por el módulo de pruebas, pero no demuestra que el sistema físico funcione.

## 5. Actividades de debugging pendientes

Para completar el proceso de depuración solicitado en la sesión 4, queda pendiente:

1. Ejecutar y documentar un intento de reproducir un fallo o un caso límite.
2. Registrar la entrada utilizada y la salida observada.
3. Formular una hipótesis y comprobarla.
4. Documentar una corrección si se identifica un problema.
5. Ejecutar nuevamente las pruebas para verificar que no se hayan introducido regresiones.
6. Registrar cualquier consulta real realizada a una herramienta de IA durante la depuración.

## 6. Conclusión

Se dispone de evidencia de ocho pruebas automatizadas satisfactorias. La depuración de un fallo reproducible, la validación de cualquier corrección y las pruebas físicas del sistema continúan pendientes. No se afirma que se haya corregido un fallo que no haya sido reproducido.
## 7. Prueba controlada de entrada inválida

- **Objetivo:** comprobar cómo responde la función ante una lectura de humedad que no es numérica.
- **Función evaluada:** `decide_watering()`.
- **Entrada utilizada:** `'invalido'`, con `tank_has_water=True`.
- **Comando ejecutado:** `py -c "from control import decide_watering; print(decide_watering('invalido', True))"`
- **Resultado observado:** `Decision(pump_on=False, reason='humedad_invalida')`.
- **Interpretación:** la función rechazó la lectura inválida, mantuvo la bomba apagada y devolvió una razón descriptiva sin generar una excepción.
- **Conclusión:** el caso probado se maneja de forma controlada. Esta prueba no demuestra el funcionamiento del hardware físico.
