# Arquitectura del sistema

## Flujo de funcionamiento

1. El sensor capacitivo entrega una lectura analógica.
2. El programa convierte la lectura a un porcentaje relativo de humedad.
3. El flotador informa si hay agua disponible en el tanque.
4. La función `decide_watering()` aplica el modo y el umbral configurados.
5. La salida GPIO25 entrega una señal lógica al driver de potencia.
6. El driver controla la alimentación de la bomba.

## Reglas de control

- **Automático:** activa la bomba cuando la humedad estimada está por debajo del umbral y hay agua disponible.
- **Manual:** activa la bomba solo cuando hay una solicitud manual y hay agua disponible.
- **Seguridad:** tanque vacío siempre bloquea la bomba, incluso si se solicita encendido manual.
- **Parada:** al interrumpir el programa, la salida de control se establece en apagado.

## Separación de responsabilidades

- `main.py`: comunicación con sensores, salida al driver y ciclo principal.
- `src/control.py`: reglas de decisión, sin depender de hardware.
- `tests/test_control.py`: pruebas de la lógica usando Python estándar.

## Limitaciones conocidas

La conversión del sensor requiere calibración. El porcentaje es aproximado. La compatibilidad eléctrica del driver, la corriente de arranque de la bomba y el montaje físico deben verificarse por separado.
