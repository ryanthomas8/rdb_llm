#!/bin/bash

# Activate the virtual environment
source scripts/venv-init.sh

# Run the PostgreSQL Docker container
docker run --rm --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres

# Wait for the PostgreSQL container to be ready
echo "Waiting for PostgreSQL to start..."
until docker exec some-postgres pg_isready -U postgres; do
  sleep 1
done

# Run Alembic migrations
echo "Running Alembic migrations..."
alembic upgrade head

# Load sample data into the database
echo "Loading sample data..."
python scripts/load_sample_data.py

# Run the Ollama Docker container
docker run -d --rm --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Wait for the Ollama container to be responsive
echo "Waiting for Ollama API to be available..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 2
done

# Pull the gemma2 model
echo "Pulling gemma2 model..."
docker exec -it ollama ollama pull gemma2

# Ensure the gemma2 model is loaded
echo "Waiting for gemma2 model to be available..."
until docker exec -it ollama ollama list | grep -q "gemma2"; do
  sleep 2
done

# Start the FastAPI app
uvicorn app.app:app --reload
