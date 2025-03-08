# Activate the virtual environment
source scripts/venv-init.sh

# Run the PostgreSQL Docker container
docker run --rm --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres

# Wait for the PostgreSQL container to be ready (optional but recommended)
# You might want to add a wait or delay for PostgreSQL to be fully started
echo "Waiting for PostgreSQL to start..."
sleep 5  # Adjust the sleep time if needed to allow PostgreSQL to initialize

# Run Alembic migrations
echo "Running Alembic migrations..."
alembic upgrade head

# Load sample data into the database
echo "Loading sample data..."
python scripts/load_sample_data.py

echo "Script execution completed."
