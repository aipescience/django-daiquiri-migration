#!/usr/bin/env python

import json
import MySQLdb

import settings

# init fixture list (will be serialized to json at the end)
fixtures = []

# get a connection to the daiquiri database
daiquiri_connection = MySQLdb.connect(**settings.LEGACY_DATABASE)
daiquiri_cursor = daiquiri_connection.cursor()

# query all messages from the daiquiri database
daiquiri_cursor.execute('''
    SELECT e.id, e.name, e.query, e.description, e.publication_role_id, e.order, r.role
    FROM Query_Examples AS e
    JOIN Auth_Roles AS r ON e.publication_role_id = r.id
''')

# fetch users and create fixtures for every user, profile and email address (for allauth)
for example_id, name, query, description, role_id, order, role in daiquiri_cursor.fetchall():

    if role == 'guest':
        access_level = 'PUBLIC'
        groups = []
    elif role == 'user':
        access_level = 'INTERNAL'
        groups = []
    else:
        access_level = 'PRIVATE'
        groups = [role_id]

    # create a contactmessage fixture
    fixtures.append({
        'model': 'daiquiri_query.example',
        'pk': example_id,
        'fields': {
            'order': order,
            'name': name,
            'description': description,
            'query_language': settings.QUERY_EXAMPLE_LANGUAGE,
            'query_string': query,
            'access_level': access_level,
            'groups': groups
        }
    })

print(json.dumps(fixtures, indent=2, sort_keys=True))
