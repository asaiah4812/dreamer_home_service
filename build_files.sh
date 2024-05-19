# Use pyenv to install dependencies
pyenv exec pip install -r requirements.txt

# Use pyenv to run manage.py collectstatic
pyenv exec python manage.py collectstatic