#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@admin.com"}
cd /app/

python manage.py migrate --noinput

python manage.py createsuperuser --username $SUPERUSER_EMAIL --email $SUPERUSER_EMAIL --noinput || true