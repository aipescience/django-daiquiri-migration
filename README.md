Migration scripts for Daiquiri
==============================

The scripts in this repository can be used to convert a service using the legacy [PHP Daiquiri](https://github.com/aipescience/daiquiri) to the new [Django Daiquiri](https://github.com/aipescience/django-daiquiri).

Setup
-----

Create a virtual enviroment and install the python dependecies:

```
python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```

Next, create a `settings.py` file and edit for the connection to the legacy Daiquiri database.

```
cp sample.settings.py settings.py
```

Usage
-----

The different scripts read parts of the legacy Daiquiri database and create Django fixtures, which they output to `stdout` as JSON. Files can be created using redirects:

```
./create_auth_fixtures.py > auth.json
./create_contact_fixtures.py > contact.json
./create_query_fixtures.py > query.json
```

The fixtures can then be loaded into the new Daiquiri instace using:

```
python manage.py loaddata <fixture>
```

inside project directory (and activated virtual enviroment) of the already set up Daiquiri app.
