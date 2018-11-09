#!/usr/bin/env python

import json
import MySQLdb

from datetime import timedelta

import settings

# init fixture list (will be serialized to json at the end)
fixtures = []

# get a connection to the daiquiri database
daiquiri_connection = MySQLdb.connect(**settings.LEGACY_DATABASE)
daiquiri_cursor = daiquiri_connection.cursor()

# query all messages from the daiquiri database
daiquiri_cursor.execute('''
    SELECT id, firstname, lastname, email, subject, message, `datetime`, status_id, user_id
    FROM Contact_Messages
''')

# fetch users and create fixtures for every user, profile and email address (for allauth)
for row in daiquiri_cursor.fetchall():
    message_id, first_name, last_name, email, subject, message, created, status_id, user_id = row

    author = '%s %s' % (first_name, last_name)
    status = 'ACTIVE' if status_id == 1 else 'CLOSED'

    if created:
        created = (created - timedelta(hours=1)).isoformat() + 'Z'
    else:
        created = settings.DEFAULT_CONTRACT_MESSAGE_DATE

    user_id = user_id if user_id > 0 else None

    # create a contactmessage fixture
    fixtures.append({
        'model': 'daiquiri_contact.contactmessage',
        'pk': message_id,
        'fields': {
            'author': author,
            'email': email,
            'subject': subject,
            'user': user_id,
            'status': status,
            'created': created,
            'message': message
        }
    })

print(json.dumps(fixtures, indent=2, sort_keys=True))
