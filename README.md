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
./fetch_contact_messages > messages.json
./fetch_groups.py > groups.json
./fetch_query_examples.py > examples.json
./fetch_query_jobs.py > jobs.json
./fetch_users.py > users.json
```

The fixtures can then be loaded into the new Daiquiri instace using:

```
python manage.py loaddata <fixture>
```

inside project directory (and activated virtual enviroment) of the already set up Daiquiri app. `groups.json` needs to be loaded first, then `users.json`, and the the other fixtures.
