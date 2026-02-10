import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

# Lädt die .env Datei
load_dotenv()

@dataclass(frozen=True)
class Settings:
    database_url: str
    inbox_dir: Path
    archive_dir: Path
    rejects_dir: Path
    ollama_base_url: str
    ollama_model: str

def load_settings() -> Settings:
    return Settings(
        database_url=os.getenv("DATABASE_URL", ""),
        inbox_dir=Path(os.getenv("INBOX_DIR", "data/inbox")),
        archive_dir=Path(os.getenv("ARCHIVE_DIR", "data/archive")),
        rejects_dir=Path(os.getenv("REJECTS_DIR", "data/rejects")),
        ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        ollama_model=os.getenv("OLLAMA_MODEL", "llama3.1"),
    )