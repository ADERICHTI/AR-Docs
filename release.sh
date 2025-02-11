#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart the server (if applicable)
# Example for Gunicorn
sudo systemctl restart gunicorn

