#!/bin/bash

python manage.py migrate

python manage.py collectstatic --noinput

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@example.com"}
SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-"adminpassword"}
SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-"admin"}

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser('${SUPERUSER_USERNAME}', '${SUPERUSER_EMAIL}', '${SUPERUSER_PASSWORD}')
EOF
