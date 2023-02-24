web: gunicorn eduplus.wsgi:application --preload
worker: celery worker --app=eduplus --loglevel=info -B
release: python3 manage.py migrate
