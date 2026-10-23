import json
import tempfile
import unittest
from pathlib import Path
from src.registro import registrar_evento, leer_eventos

class TestRegistro(unittest.TestCase):
    def test_registra_evento(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'eventos.jsonl'; self.assertTrue(registrar_evento({'codigo':'OK'},p)); self.assertTrue(p.exists())
    def test_lee_evento(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'eventos.jsonl'; registrar_evento({'codigo':'OK'},p); self.assertEqual(leer_eventos(p)[0]['codigo'],'OK')
    def test_archivo_inexistente(self):
        with tempfile.TemporaryDirectory() as d: self.assertEqual(leer_eventos(Path(d)/'no.jsonl'), [])
    def test_dos_eventos(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'eventos.jsonl'; registrar_evento({'n':1},p); registrar_evento({'n':2},p); self.assertEqual(len(leer_eventos(p)),2)
    def test_registro_rechaza_ruta_invalida(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'archivo'; p.write_text('x',encoding='utf-8')
            self.assertFalse(registrar_evento({'x':1},p/'subarchivo'))

if __name__ == '__main__': unittest.main()
