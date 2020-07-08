#!/bin/sh

# Run the Flask app with uwsgi
source venv/bin/activate
flask db upgrade
flask translate compile
exec gunicorn -b :8003 --access-logfile - --error-logfile - main:app