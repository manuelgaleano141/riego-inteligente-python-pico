import unittest
from control import decide_watering

class TestControl(unittest.TestCase):
    def test_dry_soil(self): self.assertTrue(decide_watering(20, True).pump_on)
    def test_moist_soil(self): self.assertFalse(decide_watering(60, True).pump_on)
    def test_empty_tank_auto(self): self.assertFalse(decide_watering(10, False).pump_on)
    def test_empty_tank_manual(self): self.assertFalse(decide_watering(10, False, "manual", True).pump_on)
    def test_invalid_reading(self): self.assertEqual(decide_watering(101, True).reason, "humedad_fuera_de_rango")
    def test_invalid_mode(self): self.assertFalse(decide_watering(10, True, "turbo").pump_on)
    def test_invalid_type(self): self.assertEqual(decide_watering("seco", True).reason, "humedad_invalida")
    def test_manual_not_requested(self): self.assertFalse(decide_watering(10, True, "manual", False).pump_on)

if __name__ == "__main__": unittest.main()
