#!/bin/sh
alembic upgrade head
uvicorn app.app:app --host 0.0.0.0 --port 8000 --workers 4
