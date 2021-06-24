# TS: API

## Descrição

Desafio: API DRF para gerenciar itens de loja.

Construído sobre uma plataforma Python 3, Poetry, Pytest, Flake8, Python-decouple, Docker, Docker-Compose, Postgresql

## Instruções instalação e execução com docker-compose

- Configure as opções de: migrations, user_admin, pytest (com ou sem relatório) e runserver, em:

> scripts/run.sh

- No terminal execute:

```sh
docker-compose up
```

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

## Autor(es)

- Danilo
