#!/bin/bash

# Wait for the SQL server to start
sleep 10

echo "Initializing database..."
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

echo "Starting the Flask application..."
exec gunicorn -w 4 -b 0.0.0.0:5001 __init__:app
