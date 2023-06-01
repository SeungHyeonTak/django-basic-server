FROM    python:3.9.5

RUN     apt-get update && apt-get update -y
COPY    requirements.txt /app/requirements.txt
RUN     pip install -U pip
RUN     pip install -r /app/requirements.txt
COPY    . /app

WORKDIR /app

CMD     python manage.py migrate; python manage.py runserver 0:81

EXPOSE  81