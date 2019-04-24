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

Next, create a `settings.py` file from the sample template:

```
cp sample.settings.py settings.py
```

and edit the file for the connection to the different databases, where:

* `LEGACY_DATABASE` is the PHP Daiquiri (web) database,
* `DJANGO_DATABASE` is the Dajngo Daiquiri (app) database, and
* `WORDPRESS_DATABASE` ist the WordPress database.

Once `settings.py` is complete, you can use `./check.py` to check the connection to the databases.

Usage
-----

The different scripts read parts of the legacy Daiquiri database and create Django fixtures:

```
./fetch_groups.py
./fetch_users.py
./fetch_contact_messages.py
./fetch_query_examples.py
./fetch_query_jobs.py
```

The fixtures can then be loaded into the new Daiquiri instace using:

```
python manage.py loaddata <fixture>
```

Inside project directory (and activated virtual enviroment) of the already set up Daiquiri app. `groups.json` needs to be loaded first, then `users.json`, and the the other fixtures.
