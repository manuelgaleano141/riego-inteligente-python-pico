import math
import unittest
from src.control import validar_humedad, decide_watering, Decision

class TestValidarHumedad(unittest.TestCase):
    def test_lectura_cero(self): self.assertEqual(validar_humedad(0), (True, "lectura_valida"))
    def test_lectura_cien(self): self.assertTrue(validar_humedad(100)[0])
    def test_entero_valido(self): self.assertTrue(validar_humedad(35)[0])
    def test_decimal_valido(self): self.assertTrue(validar_humedad(34.5)[0])
    def test_negativo(self): self.assertEqual(validar_humedad(-1)[1], "humedad_fuera_de_rango")
    def test_mayor_cien(self): self.assertEqual(validar_humedad(101)[1], "humedad_fuera_de_rango")
    def test_texto(self): self.assertEqual(validar_humedad("35")[1], "humedad_invalida")
    def test_none(self): self.assertEqual(validar_humedad(None)[1], "humedad_invalida")
    def test_bool(self): self.assertFalse(validar_humedad(True)[0])
    def test_nan(self): self.assertFalse(validar_humedad(math.nan)[0])
    def test_infinito(self): self.assertFalse(validar_humedad(math.inf)[0])

class TestDecideWatering(unittest.TestCase):
    def test_suelo_seco(self): self.assertEqual(decide_watering(20, True), Decision(True, "suelo_seco"))
    def test_humedad_suficiente(self): self.assertEqual(decide_watering(50, True), Decision(False, "humedad_suficiente"))
    def test_umbral_igual(self): self.assertFalse(decide_watering(35, True).pump_on)
    def test_deposito_vacio(self): self.assertEqual(decide_watering(20, False).reason, "deposito_vacio")
    def test_modo_invalido(self): self.assertEqual(decide_watering(20, True, mode="otro").reason, "modo_invalido")
    def test_nivel_invalido(self): self.assertEqual(decide_watering(20, 1).reason, "nivel_invalido")
    def test_humedad_invalida(self): self.assertFalse(decide_watering(150, True).pump_on)
    def test_umbral_invalido(self): self.assertEqual(decide_watering(20, True, threshold_percent=101).reason, "umbral_invalido")
    def test_manual_activado(self): self.assertTrue(decide_watering(50, True, mode="manual", manual_request=True).pump_on)
    def test_manual_desactivado(self): self.assertFalse(decide_watering(20, True, mode="manual", manual_request=False).pump_on)

if __name__ == '__main__': unittest.main()
