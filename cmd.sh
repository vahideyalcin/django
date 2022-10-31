python manage.py makemigrations
python manage.py migrate
kill -9 $(lsof -t -i:8000) || echo "Port zaten temiz."
python manage.py runserver 8000

