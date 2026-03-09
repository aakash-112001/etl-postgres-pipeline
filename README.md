# ETL Postgres Pipeline

A simple end-to-end ETL pipeline built using:

- Python
- Pandas
- SQLAlchemy
- PostgreSQL (Docker)
- WSL2
- Git

## Architecture

CSV → Transform (Pandas) → Load to PostgreSQL

## Run Locally

1. Start Postgres container
2. Activate virtual environment
3. Run:

```bash
python -m src.main
