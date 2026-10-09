from __future__ import annotations

import sys
import zipfile
from pathlib import Path, PurePosixPath

ARCHIVE = Path("EMA_MAYOREO_WEB_LISTO_PARA_SUBIR.zip")
DEST = Path(".deploy_src")
REQUIRED = (
    "web_server.py",
    "data_engine.py",
    "VERSION.txt",
    "requirements.txt",
    "init_persistent_data.py",
    "web/index.html",
    "web/app.js",
    "data/canonical.json",
    "data/audit.json",
    "data/locations.json",
    "tools/rebuild_data.py",
)
FORBIDDEN_SUFFIXES = {".xlsx", ".xls", ".db", ".sqlite", ".sqlite3", ".pyc", ".pyo"}


def main() -> int:
    if not ARCHIVE.is_file():
        print(f"Falta {ARCHIVE.name} en la raíz del repositorio.", file=sys.stderr)
        return 2

    try:
        with zipfile.ZipFile(ARCHIVE) as archive:
            members = archive.infolist()
            for member in members:
                path = PurePosixPath(member.filename)
                if path.is_absolute() or ".." in path.parts or "\\" in member.filename:
                    raise ValueError(f"Ruta insegura: {member.filename}")
                if any(part.lower() in {"runtime", "__pycache__"} for part in path.parts):
                    raise ValueError(f"Runtime/binarios no permitidos: {member.filename}")
                if Path(member.filename).suffix.lower() in FORBIDDEN_SUFFIXES:
                    raise ValueError(f"Archivo de datos/binario no permitido: {member.filename}")

            DEST.mkdir(parents=True, exist_ok=True)
            archive.extractall(DEST)

        missing = [name for name in REQUIRED if not (DEST / name).is_file()]
        if missing:
            raise ValueError("Faltan archivos requeridos: " + ", ".join(missing))

        print(f"Paquete EMA validado: {len(members)} archivos.")
        return 0
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        print(f"Error preparando EMA: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
