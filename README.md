Project name: **_ColudBookWriting_**

1: **making environment and installing all packages**
install python
install pipenv using command pip on terminal(pip install pipenv)
then hit command (pipenv install)
pipenv automatically creates and env and install all packages from Pipfile

2: **activating .venv:**
(pipenv --venv) this command returns that enviroment path so select interpreter from there.
then (pipenv shell) automatically activate the environment

**Run the Application and API**
Make sure to activate the virtual environment
​use command: python manage.py runserver
by default port will be 8000 but you can specify any other port number
like (python manage.py runserver 9000)
