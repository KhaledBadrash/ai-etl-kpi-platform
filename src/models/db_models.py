# src/models/db_models.py

# Standard-Bibliotheken
from datetime import datetime

# SQLAlchemy Typen & Mapping
# String, Integer etc.: SQL-Datentypen
# ForeignKey: Verknüpfung zwischen Tabellen (Relationen)
# JSON: Speichert flexible Datenstrukturen
# Mapped/mapped_column: Modernes Type-Hinting für Spalten
from sqlalchemy import String, Integer, DateTime, Text, Float, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from src.utils.db import Base

# --- TABELLE: ETL Run Log (Meta-Daten) ---
# Protokolliert jeden Pipeline-Durchlauf (Status, Zeitstempel)
class EtlRun(Base):
    __tablename__ = "etl_runs"  # Name in Postgres

    # Primärschlüssel (Auto-Increment)
    run_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Startzeitpunkt (Default: Jetzt)
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    # Status-Flag (running, success, failed)
    status: Mapped[str] = mapped_column(String(32), default="running")

# --- TABELLE: Bronze Layer (Raw Data) ---
# Unveränderte Rohdaten aus Quellen (Excel/JSON)
# Dient als "Single Source of Truth" & Backup
class StgRawRow(Base):
    __tablename__ = "stg_raw_rows"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # FK -> Referenz zum ETL-Lauf
    run_id: Mapped[int] = mapped_column(ForeignKey("etl_runs.run_id"))
    # Herkunfts-Hinweis (z.B. Dateiname oder Sheet-Name)
    entity_hint: Mapped[str] = mapped_column(String(64)) 
    # Payload -> Komplette Zeile als JSON-Objekt (Schema-less)
    raw_payload: Mapped[dict] = mapped_column(JSON)
    # Zeitstempel der Erfassung
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

# --- TABELLE: Silver Layer (Canonical) ---
# Bereinigte, typisierte Business-Objekte (hier: Projekte)
class CanonicalProject(Base):
    __tablename__ = "canonical_project"
    
    # Fachlicher Schlüssel (Business Key) als PK
    project_id: Mapped[str] = mapped_column(String(64), primary_key=True)
    # Projektname (Max 255 Zeichen)
    name: Mapped[str] = mapped_column(String(255))
    # Budget (Nullable -> kann leer sein)
    budget: Mapped[float] = mapped_column(Float, nullable=True) 
    # Letzte Änderung (für Versionierung/Update-Logik)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)