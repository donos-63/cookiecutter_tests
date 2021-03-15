# This is a simple Dockerfile to use while developing
# It's not suitable for production

FROM python:{{ cookiecutter.python_version }}

RUN mkdir /code
WORKDIR /code

COPY requirements.txt setup.py tox.ini ./
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install -e .

COPY {{ cookiecutter.app_name }} {{ cookiecutter.app_name }}/
COPY migrations migrations/

EXPOSE 5000
