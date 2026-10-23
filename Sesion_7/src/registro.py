import json
from pathlib import Path

def registrar_evento(evento, archivo=None):
    ruta = Path(archivo) if archivo else Path(__file__).resolve().parent.parent / "registro_eventos.jsonl"
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("a", encoding="utf-8") as f:
            f.write(json.dumps(evento, ensure_ascii=False, default=str) + "\n")
        return True
    except (OSError, TypeError, ValueError) as exc:
        print(f"ERROR: no se pudo registrar el evento: {exc}")
        return False

def leer_eventos(archivo=None):
    ruta = Path(archivo) if archivo else Path(__file__).resolve().parent.parent / "registro_eventos.jsonl"
    if not ruta.exists():
        return []
    eventos = []
    try:
        with ruta.open("r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    eventos.append(json.loads(linea))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: no se pudieron leer los eventos: {exc}")
    return eventos
