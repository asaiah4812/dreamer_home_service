# build_files.sh

pip install -r requirements.txt
python3.11 manage.py collectstatic
python3.11 manage.py makemigrations
python3.11 manage.py migrate