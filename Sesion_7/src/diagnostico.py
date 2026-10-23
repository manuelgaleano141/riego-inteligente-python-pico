from datetime import datetime, timezone
import math

def diagnosticar_humedad(valor):
    evento = {"timestamp": datetime.now(timezone.utc).isoformat(), "valor": valor}
    if valor is None:
        nivel, codigo, mensaje = "error", "LECTURA_AUSENTE", "No se recibió lectura de humedad."
    elif not isinstance(valor, (int, float)) or isinstance(valor, bool):
        nivel, codigo, mensaje = "error", "TIPO_INVALIDO", "La lectura debe ser numérica."
    elif not math.isfinite(valor):
        nivel, codigo, mensaje = "error", "LECTURA_NO_FINITA", "La lectura no es finita."
    elif valor < 0 or valor > 100:
        nivel, codigo, mensaje = "error", "HUMEDAD_FUERA_DE_RANGO", "La humedad debe estar entre 0 y 100 %."
    elif valor < 35:
        nivel, codigo, mensaje = "advertencia", "HUMEDAD_BAJA", "La humedad está por debajo del umbral de referencia."
    elif valor > 80:
        nivel, codigo, mensaje = "advertencia", "HUMEDAD_ALTA", "La humedad está elevada."
    else:
        nivel, codigo, mensaje = "info", "LECTURA_VALIDA", "Lectura dentro del rango válido."
    evento.update({"nivel": nivel, "codigo": codigo, "mensaje": mensaje})
    return evento
