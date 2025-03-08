# Define the virtual environment directory
VENV_DIR=".venv"

# Navigate to the project root directory
SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
cd "$SCRIPT_DIR/.."

# Set database environment variables
export DB_USER="postgres"
export DB_PASSWORD="mysecretpassword"
export DB_HOST="localhost"
export DB_PORT="5432"
export DB_NAME="postgres"
export DATABASE_URL_DEV="postgresql+psycopg2://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"
export DATABASE_URL_TEST="postgres+psycopg2://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"
export DATABASE_URL_PROD="postgresql+psycopg2://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"
export APP_ENV="dev"

export OLLAMA_URL="http://localhost:11434/v1/"
export OLLAMA_API_KEY="ollama"

# Set the PYTHONPATH to include the /app directory
export PYTHONPATH="$PYTHONPATH:$(pwd)/app"

# Create a virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists in $VENV_DIR. Skipping creation."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies from requirements.txt if it exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

echo "Python environment setup is complete."
