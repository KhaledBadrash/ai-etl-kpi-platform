# scripts/init_db.py

# System-Module
# sys/os: Zugriff auf Dateisystem & Pfade
import sys
import os

# Pfad-Erweiterung (Hack)
# Fügt Root-Verzeichnis zum Python-Path hinzu
# Notwendig, damit 'src'-Module gefunden werden
sys.path.append(os.getcwd())

# Projekt-Module
# engine: DB-Verbindung
# Base: Enthält Meta-Daten aller Modelle
# db_models: Muss importiert werden, damit Modelle registriert sind (noqa -> linter ignorieren)
from src.utils.db import engine, Base
from src.models import db_models  # noqa: F401

def main():
    print("⏳ Initialisierung: Prüfe Schema & Verbindung...")
    
    # DDL-Generierung (Data Definition Language)
    # Erstellt fehlende Tabellen basierend auf Base-Subklassen
    # create_all -> Prüft Existenz, erstellt nur falls nötig (idempotent)
    Base.metadata.create_all(engine)
    
    print("✅ Success: DB-Schema synchronisiert.")

if __name__ == "__main__":
    main()