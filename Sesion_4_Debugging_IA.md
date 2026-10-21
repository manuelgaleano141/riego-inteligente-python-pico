# Sesión 4 — Debugging con IA
**Integrantes:** Emmanuel Franco Lopez y Manuel Galeano Alarcon  
**Estado:** plan de depuración. No se inventan fallos reales ni evidencias.

## Módulo ejecutable
La lógica preliminar está en `../src/control.py`. Ejecutar desde la raíz:
```bash
python -m unittest discover -s tests -v
```

## Pruebas documentadas
1. Suelo seco y tanque lleno solicita riego.
2. Suelo húmedo no activa bomba.
3. Tanque vacío bloquea modo automático.
4. Tanque vacío bloquea modo manual.
5. Humedad fuera de rango se rechaza.
6. Modo inválido se rechaza.
7. Tipo de dato inválido se rechaza.
8. Modo manual sin solicitud mantiene bomba apagada.

**Estado:** casos definidos; deben ejecutarse y registrarse los resultados reales.

## Intento de ruptura propuesto
Solicitar riego manual con depósito vacío y humedad baja. Esperado: bomba bloqueada. Pendiente de ejecutar.

## Registro de debugging
Por cada fallo real, registrar fecha/commit, comportamiento observado, pasos para reproducir, salida real, hipótesis, consulta a IA, cambio aplicado, prueba antes/después y regresión.

## Evidencia
Guardar salida real de la suite o capturas en `evidencias/`. No sustituirla por resultados inventados.

## Guion de defensa oral (2 minutos)
“Somos Emmanuel Franco Lopez y Manuel Galeano Alarcon. Proponemos un sistema con Raspberry Pi Pico y MicroPython que lea humedad, controle una bomba con límites de tiempo y bloquee el riego si el depósito está vacío. La lógica se separa del hardware para probar condiciones antes del montaje. Todavía no hemos comprado ni probado físicamente los componentes, por lo que distinguimos los casos definidos de los ejecutados. Los próximos pasos son correr las pruebas de software, registrar cualquier fallo real, corregirlo con cambios controlados y validar sensor, bomba, fuente y protecciones.”
