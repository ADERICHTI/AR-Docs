#!/bin/bash

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
