sudo pip install Django

cd a la carpeta

python3 manage.py migrate

python3 manage.py runserver

ir a http://localhost:8000/timetracker/



Para reiniciar los datos:
python3 manage.py migrate psatimetracker zero
python3 manage.py migrate




Para behave:

pip install behave --user
pip install behave-django

correr las pruebas:
python3 manage.py behave
