from dataclasses import dataclass

@dataclass
class Decision:
    pump_on: bool
    reason: str

def decide_watering(moisture_percent, tank_has_water, mode="auto",
                    manual_request=False, threshold_percent=35):
    if mode not in ("auto", "manual"):
        return Decision(False, "modo_invalido")
    if not isinstance(tank_has_water, bool):
        return Decision(False, "nivel_invalido")
    if not isinstance(moisture_percent, (int, float)) or isinstance(moisture_percent, bool):
        return Decision(False, "humedad_invalida")
    if not 0 <= moisture_percent <= 100:
        return Decision(False, "humedad_fuera_de_rango")
    if not isinstance(threshold_percent, (int, float)) or not 0 <= threshold_percent <= 100:
        return Decision(False, "umbral_invalido")
    if not tank_has_water:
        return Decision(False, "deposito_vacio")
    if mode == "manual":
        return Decision(bool(manual_request), "riego_manual" if manual_request else "manual_sin_solicitud")
    return Decision(moisture_percent < threshold_percent,
                    "suelo_seco" if moisture_percent < threshold_percent else "humedad_suficiente")
