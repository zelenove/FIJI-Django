To get started:

1. Create a python venv called env using the command:
    $ python3 -m venv env

2. Start the venv by running:
    $ source env/bin/activate

3. Finally, while in the venv install the requirements.tx using the command:
    (env)$ pip install -r requirements.txt

4. Start the server by running:
    (env)$ python manage.py runserver

5. Exiting the virtualenv:
    (env)$ deactivate

UWSGI and NGINX commands:

Statrting uwsgi from a virtual env:
    (env)$ uwsgi --ini django.ini --pidfile=uwsgi.pid

Stopping the server:
    (env)$ uwsgi --stop uwsgi.pid

Nginx:
    $ sudo service nginx {restart|stop|start}