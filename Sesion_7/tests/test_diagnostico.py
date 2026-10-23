import math
import unittest
from src.diagnostico import diagnosticar_humedad

class TestDiagnostico(unittest.TestCase):
    def test_ausente(self): self.assertEqual(diagnosticar_humedad(None)['codigo'], 'LECTURA_AUSENTE')
    def test_tipo_invalido(self): self.assertEqual(diagnosticar_humedad('abc')['codigo'], 'TIPO_INVALIDO')
    def test_no_finita(self): self.assertEqual(diagnosticar_humedad(math.nan)['codigo'], 'LECTURA_NO_FINITA')
    def test_fuera_de_rango_baja(self): self.assertEqual(diagnosticar_humedad(-1)['codigo'], 'HUMEDAD_FUERA_DE_RANGO')
    def test_fuera_de_rango_alta(self): self.assertEqual(diagnosticar_humedad(101)['codigo'], 'HUMEDAD_FUERA_DE_RANGO')
    def test_humedad_baja(self): self.assertEqual(diagnosticar_humedad(20)['codigo'], 'HUMEDAD_BAJA')
    def test_humedad_alta(self): self.assertEqual(diagnosticar_humedad(90)['codigo'], 'HUMEDAD_ALTA')
    def test_valida(self): self.assertEqual(diagnosticar_humedad(50)['codigo'], 'LECTURA_VALIDA')

if __name__ == '__main__': unittest.main()
