# Sistema de Riego Inteligente Automatizado

**Proyecto académico:** Sistema de Riego Inteligente Automatizado con MicroPython  
**Autor:** Manuel Galeano Alarcón  
**Plataforma usada en las pruebas recientes:** ESP32 DevKit V1  
**Entorno:** Thonny + MicroPython

## Descripción

El sistema mide la humedad del suelo y el nivel de agua disponible en el tanque. Con base en un umbral configurable, decide si debe activar la bomba de riego. Incluye modo automático y modo manual, y una regla de seguridad: **la bomba no debe encenderse si el tanque está vacío**.

> Nota de plataforma: el proyecto se planteó inicialmente para Raspberry Pi Pico, pero las pruebas físicas recientes se realizaron con ESP32. Verifica qué placa vas a presentar y ajusta el nombre del repositorio si es necesario.

## Funciones

- Lectura analógica del sensor capacitivo de humedad.
- Conversión de la lectura a un porcentaje aproximado de humedad.
- Lectura de un interruptor/flotador de nivel del tanque.
- Modo automático y modo manual.
- Umbral de humedad configurable.
- Bloqueo de la bomba cuando el tanque está vacío.
- Separación entre lógica de decisión y control del hardware.
- Pruebas unitarias de la lógica con Python estándar.

## Estructura del repositorio

```text
riego-inteligente-python-pico/
├── README.md
├── main.py
├── src/
│   └── control.py
├── tests/
│   └── test_control.py
├── docs/
│   ├── arquitectura.md
│   └── registro_pruebas.md
└── evidencias/
    └── README.md
```

## Conexiones usadas como referencia para ESP32

| Componente | ESP32 | Observación |
|---|---|---|
| Sensor capacitivo VCC | 3V3 | Confirmar el voltaje permitido por el sensor |
| Sensor capacitivo GND | GND | Tierra común |
| Sensor capacitivo AOUT | GPIO34 | Entrada analógica |
| Flotador del tanque | GPIO32 y GND | Configurado con `PULL_UP` |
| Señal de control del driver | GPIO25 | No conectar la bomba directamente al GPIO |
| Driver de bomba | Según el módulo | Revisar sus terminales y especificaciones |

**Seguridad eléctrica:** la bomba debe alimentarse desde una fuente adecuada y con una etapa de potencia compatible con la corriente de arranque. No alimentar la bomba desde un pin del ESP32. El módulo IRF520 puede no conmutar correctamente con una señal lógica de 3,3 V; valida el driver antes de usar el sistema. Comparte GND entre el ESP32 y el circuito de control cuando el diseño lo requiera. Apaga la fuente antes de cambiar conexiones.

## Configuración antes de ejecutar

1. Abre `main.py` en Thonny.
2. Revisa los pines y el estado lógico del flotador según el montaje real.
3. Calibra `DRY_RAW` y `WET_RAW` con lecturas reales del sensor.
4. Revisa que el driver de potencia sea compatible con la bomba y con la señal de 3,3 V.
5. Copia `main.py` y `src/control.py` al dispositivo MicroPython, o adapta las importaciones según cómo organices los archivos en la placa.
6. Ejecuta primero las pruebas de sensores y del driver con la bomba desconectada, y después realiza una prueba supervisada.

## Calibración de humedad

Los valores de ejemplo del programa (`DRY_RAW` y `WET_RAW`) son **referencias iniciales, no valores universales**. Registra la lectura en suelo seco y en suelo húmedo y reemplázalos. El porcentaje es una estimación relativa, no una medición de laboratorio.

## Pruebas de la lógica

Desde una terminal con Python instalado, en la raíz del repositorio:

```bash
python -m unittest discover -s tests -v
```

Estas pruebas comprueban la lógica de decisión sin necesitar conectar la placa ni encender la bomba.

## Uso de GitHub

1. Crea un repositorio en GitHub.
2. Descomprime esta carpeta.
3. Sube todos los archivos manteniendo la estructura.
4. Incluye capturas propias de Thonny, del montaje y de las pruebas en `evidencias/`.
5. No afirmes que una prueba física fue exitosa si no se ejecutó realmente.

## Estado de validación

Este repositorio contiene una implementación de referencia para exponer la lógica del proyecto. Las pruebas unitarias de software no demuestran por sí solas que el montaje físico esté validado. Documenta en `docs/registro_pruebas.md` los resultados que observes en tu propio hardware.
