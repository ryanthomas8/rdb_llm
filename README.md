# Postgres SQLAlchemy

## Envrionment Set up

```bash
source scripts/venv-init.sh
```

## Start

Start the Postgres database, run the Alembic migration, and load sample data.

```bash
bash start.sh
```

## Query 

Query the database `user` table

```bash
python app/query_user.py
```

## Run a local LLM

```bash
docker run -d --rm --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama pull gemma2
```

## Run FastAPI
```bash
uvicorn app:app --reload
```

## Links

* https://python.langchain.com/v0.1/docs/use_cases/sql/quickstart/