
from dataclasses import dataclass


@dataclass
class Decision:
    pump_on: bool
    reason: str


def decide_watering(
    moisture_percent,
    tank_has_water,
    mode="auto",
    manual_request=False,
    threshold_percent=35
):
    # Validar el modo de funcionamiento
    if mode not in ("auto", "manual"):
        return Decision(False, "modo_invalido")

    # Validar el estado del deposito
    if not isinstance(tank_has_water, bool):
        return Decision(False, "nivel_invalido")

    # Validar la lectura de humedad
    if (
        not isinstance(moisture_percent, (int, float))
        or isinstance(moisture_percent, bool)
    ):
        return Decision(False, "humedad_invalida")

    if not 0 <= moisture_percent <= 100:
        return Decision(False, "humedad_fuera_de_rango")

    # Validar el umbral de humedad
    if (
        not isinstance(threshold_percent, (int, float))
        or isinstance(threshold_percent, bool)
        or not 0 <= threshold_percent <= 100
    ):
        return Decision(False, "umbral_invalido")

    # No regar si el deposito esta vacio
    if not tank_has_water:
        return Decision(False, "deposito_vacio")

    # Control manual
    if mode == "manual":
        return Decision(
            bool(manual_request),
            "riego_manual" if manual_request
            else "manual_sin_solicitud"
        )

    # Control automatico segun la humedad
    pump_on = moisture_percent < threshold_percent

    return Decision(
        pump_on,
        "suelo_seco" if pump_on else "humedad_suficiente"
    )


if __name__ == "__main__":
    resultado = decide_watering(20, True)
    print(resultado)

