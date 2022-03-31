web: gunicorn Redditt.wsgi_application --log-file - -- log-level debug
python manage.py collectstatic --noinput
manage.py migrate 