# Postgres SQLAlchemy

## Envrionment Set up

```bash
source scripts/venv-init.sh
```

## Run

### Docker Compose

Run the following docker compose command to start the services

```bash
docker compose up
```

Then run the following script to load test data into the postgres db

```bash
python scripts/load_sample_data.py
```

Run the following script to pull the gemma2 model in the Ollama docker container

```bash
docker exec -it ollama ollama pull gemma2
```

To stop, press crtl+c in the terminal and run the following commmand to stop the docker containers

```bash 
docker compose down
```

### Local

Run the following command to start the application;

```bash
bash start.sh
```

* Activate the virtual environment
* Run the PostgreSQL Docker container
* Run Alembic migrations
* Load sample data into the database
* Run the Ollama Docker container
* Pull the gemma2 model
* Start the FastAPI app

To stop, press crtl+c in the terminal and run the following commmand to stop the docker containers

```bash 
docker stop ollama some-postgres
```

## Testing

### CURL

Enter the following in your terminal:

Request:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/ask' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "What employees work on the AI Research project?"
}'
```

Response:

```bash
{
  "question": "What employees work on the AI Research project?",
  "sql_query": "SELECT \"employee\".\"name\"\nFROM employee_projects\nJOIN employee ON employee_projects.\"employee_id\" = employee.id\nWHERE employee_projects.\"project_id\" = 1;",
  "query_result": "\"[('John Doe',), ('Alice Brown',)]\"",
  "final_answer": "John Doe and Alice Brown work on the AI Research project.  \n"
}
```

### SWAGGER

Visit the following FastAPI Swagger page to test the API endpoint: http://127.0.0.1:8000/docs

Enter in the following payload for the /ask POST endpoint

```bash
{
  "question": "What employees work on the AI Research project?"
}
```

## Links

* LLM to SQL: https://python.langchain.com/v0.1/docs/use_cases/sql/quickstart/
* Ollama Docker: https://hub.docker.com/r/ollama/ollama


## Other:

Quickly query postgress database

```bash
docker exec -it some-postgres psql -U postgres
```