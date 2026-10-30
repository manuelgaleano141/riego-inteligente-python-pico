import os
import sys
import unittest

# Permite ejecutar las pruebas desde la raíz del repositorio.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.control import decide_watering


class TestWateringDecision(unittest.TestCase):
    def test_auto_dry_soil_turns_pump_on(self):
        result = decide_watering(20, True, "auto", threshold_percent=35)
        self.assertTrue(result.pump_on)

    def test_auto_moist_soil_keeps_pump_off(self):
        result = decide_watering(60, True, "auto", threshold_percent=35)
        self.assertFalse(result.pump_on)

    def test_empty_tank_blocks_auto_mode(self):
        result = decide_watering(10, False, "auto")
        self.assertFalse(result.pump_on)

    def test_manual_request_turns_pump_on_when_water_available(self):
        result = decide_watering(
            70, True, "manual", manual_request=True
        )
        self.assertTrue(result.pump_on)

    def test_manual_without_request_keeps_pump_off(self):
        result = decide_watering(
            10, True, "manual", manual_request=False
        )
        self.assertFalse(result.pump_on)

    def test_empty_tank_blocks_manual_mode(self):
        result = decide_watering(
            10, False, "manual", manual_request=True
        )
        self.assertFalse(result.pump_on)

    def test_invalid_moisture_range_raises_value_error(self):
        with self.assertRaises(ValueError):
            decide_watering(120, True)

    def test_invalid_mode_raises_value_error(self):
        with self.assertRaises(ValueError):
            decide_watering(20, True, "automatic")

    def test_non_numeric_moisture_raises_type_error(self):
        with self.assertRaises(TypeError):
            decide_watering("seco", True)

    def test_invalid_threshold_raises_value_error(self):
        with self.assertRaises(ValueError):
            decide_watering(20, True, threshold_percent=-1)


if __name__ == "__main__":
    unittest.main()
