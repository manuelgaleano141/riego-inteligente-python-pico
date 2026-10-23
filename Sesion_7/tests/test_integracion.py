import tempfile
import unittest
from pathlib import Path
from src.sistema import procesar_lectura

class TestIntegracion(unittest.TestCase):
    def test_lectura_fuera_de_rango_no_activa_bomba(self):
        with tempfile.TemporaryDirectory() as d:
            r=procesar_lectura(150,True,archivo_registro=Path(d)/'e.jsonl'); self.assertFalse(r.pump_on)
    def test_humedad_baja_activa_bomba(self):
        with tempfile.TemporaryDirectory() as d:
            r=procesar_lectura(20,True,archivo_registro=Path(d)/'e.jsonl'); self.assertTrue(r.pump_on)
    def test_deposito_vacio_no_activa_bomba(self):
        with tempfile.TemporaryDirectory() as d:
            r=procesar_lectura(20,False,archivo_registro=Path(d)/'e.jsonl'); self.assertFalse(r.pump_on)
    def test_lectura_ausente_no_activa_bomba(self):
        with tempfile.TemporaryDirectory() as d:
            r=procesar_lectura(None,True,archivo_registro=Path(d)/'e.jsonl'); self.assertFalse(r.pump_on)

if __name__ == '__main__': unittest.main()
