from dataclasses import dataclass
import math

@dataclass
class Decision:
    pump_on: bool
    reason: str

def validar_humedad(moisture_percent):
    if not isinstance(moisture_percent, (int, float)) or isinstance(moisture_percent, bool):
        return False, "humedad_invalida"
    if not math.isfinite(moisture_percent):
        return False, "humedad_invalida"
    if not 0 <= moisture_percent <= 100:
        return False, "humedad_fuera_de_rango"
    return True, "lectura_valida"

def decide_watering(moisture_percent, tank_has_water, mode="auto", manual_request=False, threshold_percent=35):
    if mode not in ("auto", "manual"):
        return Decision(False, "modo_invalido")
    if not isinstance(tank_has_water, bool):
        return Decision(False, "nivel_invalido")
    humedad_valida, motivo = validar_humedad(moisture_percent)
    if not humedad_valida:
        return Decision(False, motivo)
    if (not isinstance(threshold_percent, (int, float)) or isinstance(threshold_percent, bool)
            or not math.isfinite(threshold_percent) or not 0 <= threshold_percent <= 100):
        return Decision(False, "umbral_invalido")
    if not tank_has_water:
        return Decision(False, "deposito_vacio")
    if mode == "manual":
        return Decision(bool(manual_request), "riego_manual" if manual_request else "manual_sin_solicitud")
    pump_on = moisture_percent < threshold_percent
    return Decision(pump_on, "suelo_seco" if pump_on else "humedad_suficiente")

def decidir_con_reintentos(lecturas, tank_has_water, mode="auto", manual_request=False, threshold_percent=35, max_attempts=3):
    if not isinstance(max_attempts, int) or isinstance(max_attempts, bool) or max_attempts < 1:
        return Decision(False, "intentos_invalidos")
    for intento, lectura in enumerate(lecturas, start=1):
        if intento > max_attempts:
            break
        humedad_valida, motivo = validar_humedad(lectura)
        if not humedad_valida:
            print(f"ERROR: lectura {lectura!r}. Motivo: {motivo}. Intento {intento} de {max_attempts}.")
            if intento < max_attempts:
                print("Reintentando lectura...")
            else:
                print("No quedan mas intentos.")
            continue
        print(f"Lectura valida: {lectura}%")
        return decide_watering(lectura, tank_has_water, mode, manual_request, threshold_percent)
    print(f"ALERTA: no se obtuvo una lectura valida en {max_attempts} intentos. Bomba apagada.")
    return Decision(False, "lectura_invalida_reintentos_agotados")

if __name__ == "__main__":
    print("Prueba de decision de riego:", decide_watering(20, True))
    print("Prueba de reintentos:", decidir_con_reintentos([-15, 150, 25], True, max_attempts=3))
