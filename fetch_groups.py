#!/usr/bin/env python

import json
import MySQLdb

import settings

# init fixture list (will be serialized to json at the end)
fixtures = []

# get a connection to the daiquiri database
daiquiri_connection = MySQLdb.connect(**settings.LEGACY_DATABASE)
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
        # print some output
        print(role_id, role)

        # create a group fixture
        fixtures.append({
            'model': 'auth.group',
            'pk': role_id,
            'fields': {
                'name': role,
                'permissions': []
            }
        })

with open('groups.json', 'w') as f:
    f.write(json.dumps(fixtures, indent=2, sort_keys=True))
