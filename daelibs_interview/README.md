# The Project

This project uses an sqlite3 database which is included in the repo (so you don't have to run migrate).


## Quick Overview
-----------------

* Ensure Python 3.10 or higher
* Create Python virtualenv and install requirements from `requirements.txt`
* Start your local server


### 1. Ensure Python 3.10 or higher is installed

Latest version can be downloaded from:

https://www.python.org/downloads/

Ensure it is added to your path.

### 2. Create virtualenv and install dependencies

To create a virtualenv,
```python
python -m venv daelibs-interview
```

This will create a folder call 'daelibs-interview', then you will need to activate the environment, run:
```
daelibs-interview\Scripts\activate.bat
```
for MacOs, run:
```
source daelibs-interview/bin/activate
```

The virtual environment will be activated and you’ll see "daelibs-interview" next to the command prompt to designate that

Once done, you should cd to the dummy project root directory and run:
```
pip install -r requirements.txt
```

### 3. Start your local server
You should now be able to run the local server by
```python
python manage.py runserver
```

