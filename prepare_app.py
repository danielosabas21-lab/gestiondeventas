from __future__ import annotations
import sys, zipfile
from pathlib import Path, PurePosixPath

ARCHIVE = Path("EMA_MAYOREO_WEB_DEPLOY_SEGURO.zip")
DEST = Path(".deploy_src")
REQUIRED = ("web_server.py","data_engine.py","VERSION.txt","requirements.txt","web/index.html","web/app.js")
FORBIDDEN = {".xlsx",".xls",".db",".sqlite",".sqlite3",".pyc",".pyo"}

def main():
    if not ARCHIVE.is_file():
        print("Falta EMA_MAYOREO_WEB_DEPLOY_SEGURO.zip en la raíz del repositorio.", file=sys.stderr)
        return 2
    try:
        with zipfile.ZipFile(ARCHIVE) as z:
            members = z.infolist()
            for m in members:
                p = PurePosixPath(m.filename)
                if p.is_absolute() or ".." in p.parts or "\\" in m.filename:
                    raise ValueError("Ruta insegura: " + m.filename)
                if any(x.lower() in {"runtime","__pycache__"} for x in p.parts):
                    raise ValueError("Runtime/binarios no permitidos: " + m.filename)
                if Path(m.filename).suffix.lower() in FORBIDDEN:
                    raise ValueError("Datos sensibles/binarios no permitidos: " + m.filename)
            DEST.mkdir(parents=True, exist_ok=True)
            z.extractall(DEST)
        missing = [f for f in REQUIRED if not (DEST/f).is_file()]
        if missing: raise ValueError("Faltan archivos: " + ", ".join(missing))
        print(f"Paquete validado: {len(members)} archivos.")
        return 0
    except (OSError, zipfile.BadZipFile, ValueError) as e:
        print(f"Error preparando el paquete: {e}", file=sys.stderr)
        return 1
if __name__ == "__main__":
    raise SystemExit(main())
