"""Lógica de decisión independiente del hardware.

Este módulo usa sintaxis compatible con Python estándar y MicroPython.
"""


class Decision:
    def __init__(self, pump_on, reason):
        self.pump_on = bool(pump_on)
        self.reason = str(reason)

    def __repr__(self):
        return "Decision(pump_on={!r}, reason={!r})".format(
            self.pump_on, self.reason
        )


def decide_watering(
    moisture_percent,
    tank_has_water,
    mode="auto",
    manual_request=False,
    threshold_percent=35,
):
    """Decide si la bomba debe encenderse.

    Args:
        moisture_percent: humedad estimada entre 0 y 100.
        tank_has_water: True si hay agua disponible.
        mode: 'auto' o 'manual'.
        manual_request: petición de encendido en modo manual.
        threshold_percent: umbral a partir del cual no se necesita regar.

    Returns:
        Decision con pump_on y una explicación breve.
    """
    if isinstance(moisture_percent, bool) or not isinstance(
        moisture_percent, (int, float)
    ):
        raise TypeError("moisture_percent debe ser numérico")

    if not 0 <= moisture_percent <= 100:
        raise ValueError("moisture_percent debe estar entre 0 y 100")

    if not isinstance(tank_has_water, bool):
        raise TypeError("tank_has_water debe ser booleano")

    if mode not in ("auto", "manual"):
        raise ValueError("mode debe ser 'auto' o 'manual'")

    if isinstance(threshold_percent, bool) or not isinstance(
        threshold_percent, (int, float)
    ):
        raise TypeError("threshold_percent debe ser numérico")

    if not 0 <= threshold_percent <= 100:
        raise ValueError("threshold_percent debe estar entre 0 y 100")

    if not isinstance(manual_request, bool):
        raise TypeError("manual_request debe ser booleano")

    # La protección del tanque tiene prioridad en ambos modos.
    if not tank_has_water:
        return Decision(False, "Tanque vacío: protección activada")

    if mode == "auto":
        if moisture_percent < threshold_percent:
            return Decision(True, "Humedad inferior al umbral")
        return Decision(False, "Humedad suficiente")

    if manual_request:
        return Decision(True, "Solicitud manual autorizada")
    return Decision(False, "Sin solicitud manual")
