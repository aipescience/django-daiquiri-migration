#!/usr/bin/env python
import json
import MySQLdb

import settings

# fetch user from daiquiri
daiquiri_connection = MySQLdb.connect(**settings.DJANGO_DATABASE)

daiquiri_cursor = daiquiri_connection.cursor()
daiquiri_cursor.execute('SELECT id, details, attributes FROM daiquiri_auth_profile;')

profiles = daiquiri_cursor.fetchall()

for profile_id, details_json, attributes_json in profiles:
    details = json.loads(details_json) if details_json else {}
    attributes = json.loads(attributes_json) if attributes_json else {}

    for key in list(details):
        if key not in settings.AUTH_DETAIL_KEYS:
            attributes[key.lower()] = details.pop(key)

    daiquiri_cursor.execute('UPDATE daiquiri_auth_profile SET details = %s WHERE id = %s', (json.dumps(details), profile_id))
    daiquiri_cursor.execute('UPDATE daiquiri_auth_profile SET attributes = %s WHERE id = %s', (json.dumps(attributes), profile_id))

daiquiri_connection.commit()
