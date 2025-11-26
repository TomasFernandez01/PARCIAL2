#!/usr/bin/env bash
# build.sh

set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt


echo "Running migrations..."
python manage.py migrate
python manage.py migrate estadisticas  # ← MIGRACIÓN ESPECÍFICA
python manage.py migrate galeria
python manage.py migrate informes
python manage.py migrate shop
python manage.py migrate api_libros
python manage.py migrate scraper

echo "Collecting static files..."
python manage.py collectstatic --noinput

