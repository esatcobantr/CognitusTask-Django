python manage.py migrate
/usr/local/bin/gunicorn Cognitus_Task.wsgi:application \
    --bind :8000 \
    --reload