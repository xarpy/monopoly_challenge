# Monopoly Challenge

[![Python Version][python-image]][python-url]


System created, according to a monopoly board game challenge.

## Installation

### Environment Local

Using your dependency manager, create a python environment, follow a [link](https://ahmed-nafies.medium.com/pip-pipenv-poetry-or-conda-7d2398adbac9) talking about the managers!

Access the project folder and using the **pip** manager, inside the python env, apply the command below:

Upgrade pip version and install requirements and install:

```sh
pip install --upgrade pip && pip install --require-hashes -r requirements/dev.txt
```

After installing all dependencies,compile this project with command:

```sh
python manage.py run
```

### Docker Build

You will need to have docker-compose, and finally apply the command:

```sh
docker-compose up --build
```

After build project, in another terminal, apply the command:

```sh
docker exec -it monopoly-challenge python manage.py run
```

## Dependencies
This project uses hashed dependencies. To update them, edit `requirements/base.in` for project dependencies and `requirements/dev.in` for development dependencies and run:
```sh
pip-compile --generate-hashes --output-file requirements/base.txt requirements/base.in && \
pip-compile --generate-hashes --output-file requirements/dev.txt requirements/dev.in
```
It is always necessary to `pip-compile` both because dev-deps references base-deps.

## Usage

In order to be able to normalize, we add the best practices in this project, aiming to respect the principles with example **Clean Code**, **SOLID** and others. For more details, see the tip links!


### Formatters and Linters

* [Flake8](https://flake8.pycqa.org/en/latest/index.html)
* [Black](https://black.readthedocs.io/en/stable/)
* [Isort](https://isort.readthedocs.io/en/latest/)
* [Bandit](https://bandit.readthedocs.io/en/latest/)
* [MyPy](https://mypy.readthedocs.io/en/stable/)

**Obs:**

* Programming with Python, we use the `snake_case` style for variables, functions and methods, and the `PascalCase` style for classes. Configuration variables should written in `UPPERCASE`.

### Structure

We use the **microservices architecture patterns**, to create API resources. To example, see the content:

```sh
.
├── app
│   ├── __init__.py
│   ├── core
│   │   └── __init__.py
│   │   └── settings.py
│   ├── __init__.py
│   ├── models
│   │   ├── board.py
│   │   ├── __init__.py
│   │   └── player.py
│   ├── repositories
│   │   ├── board.py
│   │   ├── __init__.py
│   │   └── players.py
│   └── services
│       ├── game.py
│       ├── __init__.py
│       └── statistic.py
├── docker-compose.yml
├── Dockerfile
├── env.example
├── manage.py
├── pyproject.toml
├── README.md
├── requirements
│   ├── base.in
│   ├── base.txt
│   ├── dev.in
│   └── dev.txt
└── tests

```

### Tests

In this application, we used this dependencies to perform, scan and cover tests in the application:

* [Interrogate](https://interrogate.readthedocs.io/en/latest/)
* [Coverage](https://coverage.readthedocs.io/en/6.3.2/)
* [Pytest](https://docs.pytest.org/en/6.2.x/)

In this application, unit tests were created, using **pytest**. Follow the instructions to run the tests:

* To see tests list

```sh
docker-compose run monopoly-challenge python manage.py runtest --list
```

* To run all test

```sh
docker-compose run monopoly-challenge python manage.py runtest
```

* To run only test module

```sh
docker-compose run monopoly-challenge python manage.py runtest -n <module_name>.py
```

* To run only function test module

```sh
docker-compose run monopoly-challenge python manage.py runtest -n <module_name>.py::<function_teste_name>
```
**Obs:**

* If you're not used to the docker-compose tool, you can change the prefix using ``docker exec -it project python manage.py runtest --help``
* Any doubts about the use or how pytest works, in the resources section we provide a direct link to the tool's documentation.

## Tips

In this session, we include several articles related to good practices, tools and more.

* [Tips for pip-tools and multple environments](https://www.caktusgroup.com/blog/2018/09/18/python-dependency-management-pip-tools/)
* [Locking dependency with pip-tools](https://lincolnloop.com/blog/python-dependency-locking-pip-tools/)
* [Tips for environments python](https://towardsdatascience.com/virtual-environments-104c62d48c54)
* [SOLID Principle](https://medium.com/@engnogueirawgn/princ%C3%ADpios-solid-na-pr%C3%A1tica-e932608406d6)
* [Clean Code and principles](https://henriquesd.medium.com/dry-kiss-yagni-principles-1ce09d9c601f)
* [Environments python, what is have choosen?](https://ahmed-nafies.medium.com/pip-pipenv-poetry-or-conda-7d2398adbac9)
* [Overview of python dependency management tools](https://modelpredict.com/python-dependency-management-tools)
* [Types of development styles](https://betterprogramming.pub/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841)
* [Best pratices in Python](https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5?gi=6989d5c08d78)
* [Flake 8 best configurations](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html)
* [Black tips](https://www.mattlayman.com/blog/2018/python-code-black/)
* [EditorConfig tips](https://blog.matheuscastiglioni.com.br/padronizando-seus-editores-de-texto-com-editorconfig/)
* [Pre-commits tips](https://towardsdatascience.com/getting-started-with-python-pre-commit-hooks-28be2b2d09d5)
* [Pre-commits Automating](https://towardsdatascience.com/automating-python-workflows-with-pre-commit-hooks-e5ef8e8d50bb)
* [Why use Gitignore Global?](http://egorsmirnov.me/2015/05/04/global-gitignore-file.html)
* [Git Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
* [Git Semantic Version](https://semver.org/lang/pt-BR/)

## Resources and Documentations

* [Pip (Package Installer Python)](https://pip.pypa.io/en/stable/)
* [Pre-commits](https://pre-commit.com/index.html)
* [Editor Config](https://editorconfig.org/)
* [Pip Tools](https://github.com/jazzband/pip-tools)
* [Click](https://click.palletsprojects.com/en/8.1.x/)
* [Docker](https://docs.docker.com/get-started/)
* [Docker Compose](https://docs.docker.com/compose/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

[python-url]: https://www.python.org/dev/peps/pep-0596/
[python-image]: https://img.shields.io/badge/python-v3.10-blue
