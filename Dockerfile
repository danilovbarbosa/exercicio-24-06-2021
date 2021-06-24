FROM python:3.9.5
LABEL maintainer="Danilo Costa"

ENV PYTHONUNBUFFERED 1
COPY . /var/wwww
WORKDIR /var/wwww

RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

ENV PORT=8000
EXPOSE $PORT

CMD python manage.py runserver 0.0.0.0:8000