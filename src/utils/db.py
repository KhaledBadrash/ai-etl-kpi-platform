# src/utils/db.py
# create_engine: Verwaltet DB-Verbindungspool
# sessionmaker: Factory für Transaktions-Sitzungen
# DeclarativeBase: Basisklasse für Tabellen-Modelle


# import Werkzeuge SQLAlchemy --> um mit Datenbanken zu sprechen
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.utils.config import load_settings

# laden unsere Einstellungen (Passwörter, Pfade) aus der .env Datei
settings = load_settings()

# Das ist der motor --> hält die eigentliche Verbindung zur Datenbank.
# Wenn Python <--> DB 
## Zentraler Zugangspunkt zur Datenbank; verwaltet Connections
engine = create_engine(settings.database_url)

# Erstellt isolierte Sitzungen für DB-Operationen (Read/Write)
# autocommit=False -> Transaktionen müssen explizit bestätigt werden
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 4. Base 
# Alle Tabellen (Projekte, KPIs) erben von dieser Klasse, damit SQLAlchemy sie erkennt.
class Base(DeclarativeBase):
    pass


def get_session():
    return SessionLocal()