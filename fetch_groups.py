#!/usr/bin/env python

import json
import MySQLdb

from settings import DAIQUIRI_DATABASE, DATE_JOINED

# init fixture list (will be serialized to json at the end)
fixtures = []

# get a connection to the daiquiri database
daiquiri_connection = MySQLdb.connect(**DAIQUIRI_DATABASE)
daiquiri_cursor = daiquiri_connection.cursor()

# query all roles from the daiquiri database
daiquiri_cursor.execute('''
    SELECT id, role FROM Auth_Roles
''')

# fetch roles and sort into dict
groups = {}
for role_id, role in daiquiri_cursor.fetchall():

    # only add custom roles
    if role not in ['guest', 'user', 'admin']:
        fixtures.append({
            'model': 'auth.group',
            'pk': role_id,
            'fields': {
                'name': role,
                'permissions': []
            }
        })

print(json.dumps(fixtures, indent=2, sort_keys=True))
