"""
Sistema de Riego Inteligente Automatizado
MicroPython para ESP32 DevKit V1.

Antes de usar:
- Calibrar DRY_RAW y WET_RAW con el sensor real.
- Verificar el estado lógico del flotador.
- Validar el driver de la bomba y su fuente de alimentación.
"""

from machine import ADC, Pin
from time import sleep
from src.control import decide_watering

# Pines de referencia para ESP32 DevKit V1
MOISTURE_PIN = 34
TANK_FLOAT_PIN = 32
PUMP_CONTROL_PIN = 25

# Calibrar estos valores con mediciones reales.
# En muchos sensores capacitivos, la lectura disminuye al aumentar la humedad,
# pero esto debe confirmarse en el montaje utilizado.
DRY_RAW = 3000
WET_RAW = 1500

THRESHOLD_PERCENT = 35
MODE = "auto"  # "auto" o "manual"

# En este ejemplo, el driver se activa con nivel alto.
# Cambiar a False si el módulo utilizado es activo en bajo.
PUMP_ACTIVE_HIGH = True

moisture_adc = ADC(Pin(MOISTURE_PIN))
moisture_adc.atten(ADC.ATTN_11DB)
moisture_adc.width(ADC.WIDTH_12BIT)

tank_float = Pin(TANK_FLOAT_PIN, Pin.IN, Pin.PULL_UP)
pump_control = Pin(PUMP_CONTROL_PIN, Pin.OUT)


def read_moisture_percent():
    """Lee el sensor y calcula un porcentaje relativo aproximado."""
    raw = moisture_adc.read()

    if DRY_RAW == WET_RAW:
        raise ValueError("DRY_RAW y WET_RAW no pueden ser iguales")

    # La fórmula también funciona si WET_RAW es menor que DRY_RAW.
    percent = (DRY_RAW - raw) * 100 / (DRY_RAW - WET_RAW)
    percent = max(0, min(100, int(percent)))
    return raw, percent


def tank_has_water():
    """
    Con PULL_UP, un flotador conectado entre GPIO32 y GND suele leer 0
    cuando el contacto está cerrado. Confirma la lógica en tu flotador.
    """
    return tank_float.value() == 0


def set_pump(on):
    """Activa o desactiva la señal lógica que controla el driver de la bomba."""
    if PUMP_ACTIVE_HIGH:
        pump_control.value(1 if on else 0)
    else:
        pump_control.value(0 if on else 1)


def main():
    print("Sistema de Riego Inteligente iniciado")
    print("Modo:", MODE)
    print("Para cambiar el modo, edita MODE en main.py.")

    try:
        while True:
            raw, moisture = read_moisture_percent()
            water_available = tank_has_water()

            # Para modo manual, cambia MANUAL_REQUEST a True durante una
            # prueba supervisada. El ejemplo lo deja en False por seguridad.
            manual_request = False

            decision = decide_watering(
                moisture_percent=moisture,
                tank_has_water=water_available,
                mode=MODE,
                manual_request=manual_request,
                threshold_percent=THRESHOLD_PERCENT,
            )

            set_pump(decision.pump_on)

            print(
                "ADC:", raw,
                "| Humedad estimada:", str(moisture) + "%",
                "| Agua disponible:", water_available,
                "| Modo:", MODE,
                "| Bomba:", "ENCENDIDA" if decision.pump_on else "APAGADA",
                "| Motivo:", decision.reason,
            )
            sleep(2)

    except KeyboardInterrupt:
        print("Programa detenido por el usuario")
    finally:
        set_pump(False)
        print("Señal de bomba apagada")


if __name__ == "__main__":
    main()
