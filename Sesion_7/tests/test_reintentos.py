import unittest
from src.control import decidir_con_reintentos

class TestReintentos(unittest.TestCase):
    def test_lectura_valida_primera(self): self.assertTrue(decidir_con_reintentos([20], True).pump_on)
    def test_lectura_valida_despues_de_error(self): self.assertTrue(decidir_con_reintentos([-1, 20], True).pump_on)
    def test_se_agotan_intentos(self): self.assertEqual(decidir_con_reintentos([-1, 150, None], True).reason, "lectura_invalida_reintentos_agotados")
    def test_max_attempts_invalido(self): self.assertEqual(decidir_con_reintentos([20], True, max_attempts=0).reason, "intentos_invalidos")
    def test_ignora_lecturas_mas_alla_del_limite(self): self.assertEqual(decidir_con_reintentos([-1, 20], True, max_attempts=1).reason, "lectura_invalida_reintentos_agotados")

if __name__ == '__main__': unittest.main()
