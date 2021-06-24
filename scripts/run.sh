#!/bin/bash
# bash -f ./scripts/run.sh

python manage.py showmigrations

python manage.py makemigrations

python manage.py migrate

python manage.py check

# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell

# python manage.py collectstatic

coverage html -d htmlcov

pytest -v --html=htmlcov/report.html --self-contained-html
echo '''

Veja o relatório de teste disponível na pasta raiz do projeto com o nome: htmlcov/report.html

'''

python manage.py runserver 0.0.0.0:8000