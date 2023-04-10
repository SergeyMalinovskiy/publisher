# publisher

publisher

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [76e03a11268a55e7ac29d1b0352861106143e497](https://github.com/wemake-services/wemake-django-template/tree/76e03a11268a55e7ac29d1b0352861106143e497). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/76e03a11268a55e7ac29d1b0352861106143e497...master) since then.


[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake-services.github.io)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


## Prerequisites

Вам требуется:

- `python3.9` (see `pyproject.toml` for full version)
- `postgresql` with version `13`
- `docker` with [version at least](https://docs.docker.com/compose/compose-file/#compose-and-docker-compatibility-matrix) `18.02`


## Development

При разработке мы используем:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`poetry`](https://github.com/python-poetry/poetry) (**required**)
- [`pyenv`](https://github.com/pyenv/pyenv)
- `pycharm 2017+` or `vscode`

после клонирования репозитория:

Копируем файл настроек окружения, меняем DOMAIN_NAME, создаем DJANGO_SECRET_KEY
```
copy env.template to .env
```

Затем нужно запустить докер

```
export DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 # enable buildkit
docker-compose build
docker-compose run --rm web python manage.py migrate
docker-compose up
```


## Documentation

Полная документация доступна здесь: [`docs/`](docs).
