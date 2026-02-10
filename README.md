# ai-etl-kpi-platform
An automated ETL/ELT system that regularly imports raw data from Excel, JSON, and databases, converts it into a uniform canonical model, and optionally loads it into a star schema (BI-enabled). Based on this: KPI dashboard + AI insights (e.g., executive summary, anomalies, forecasts, KPI suggestions).

my_etl_project/
├── data/
│   ├── inbox/              # Hier landen Excel/JSON Files
│   ├── archive/            # Verarbeitete Files
│   └── rejects/            # Fehlerhafte Zeilen (als CSV/JSON Dump)
├── src/
│   ├── extractors/         # Logik für Excel, JSON, DB
│   ├── models/             # Pydantic Models (Canonical + Star Schema)
│   ├── transformers/       # Mapping Logik
│   ├── loaders/            # DB Insert Logic
│   └── utils/              # Logger, DB Connector
├── app.py                  # Dashboard (Streamlit)
├── main_etl.py             # Der Orchestrator (Einstiegspunkt)
├── docker-compose.yml      # Für Postgres
└── requirements.txt        # --> pip install -r requirements.txt (in powershell)

pips:
pip install ollama
ollama pull llama3.1