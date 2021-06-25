# TS: API

## Descrição

Desafio: API DRF para gerenciar itens de loja.

Construído sobre uma plataforma Python 3, Poetry, Pytest, Flake8, Python-decouple, Docker, Docker-Compose, Postgresql

## Instruções de instalação local

- Instale o Python:

```sh
pyenv local 3.9.5
```

- Configure o ambiente virtual:

```sh
poetry install
```

- Acesse o ambiente virtual:

```sh
poetry shell
```

- Execute o flake8:

```sh
flake8 .
```

- Execute as migrações:

```sh
python manage.py makemigrations
python manage.py migrate
```

- Execute o servidor:

```sh
python manage.py runserver 0.0.0.0:8001
```

## Autor(es)

- Danilo
