try:
    from .control import decide_watering, Decision
    from .diagnostico import diagnosticar_humedad
    from .registro import registrar_evento
except ImportError:  # permite ejecutar este archivo directamente
    from control import decide_watering, Decision
    from diagnostico import diagnosticar_humedad
    from registro import registrar_evento

def procesar_lectura(humedad, deposito_con_agua, modo="auto", solicitud_manual=False, umbral=35, archivo_registro=None):
    evento = diagnosticar_humedad(humedad)
    registrar_evento(evento, archivo_registro)
    if evento["codigo"] in ("TIPO_INVALIDO", "LECTURA_NO_FINITA", "LECTURA_AUSENTE"):
        return Decision(False, "humedad_invalida")
    if evento["codigo"] == "HUMEDAD_FUERA_DE_RANGO":
        return Decision(False, "humedad_fuera_de_rango")
    return decide_watering(humedad, deposito_con_agua, modo, solicitud_manual, umbral)

if __name__ == "__main__":
    print("PRUEBA DE INTEGRACION DEL SISTEMA")
    print("Humedad 150%:", procesar_lectura(150, True))
    print("Humedad 20%:", procesar_lectura(20, True))
