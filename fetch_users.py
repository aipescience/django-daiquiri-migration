#!/usr/bin/env python

import json
import MySQLdb

from settings import DAIQUIRI_DATABASE, DATE_JOINED

# init fixture list (will be serialized to json at the end)
fixtures = []

# get a connection to the daiquiri database
daiquiri_connection = MySQLdb.connect(**DAIQUIRI_DATABASE)
daiquiri_cursor = daiquiri_connection.cursor()

# query all details from the daiquiri database
daiquiri_cursor.execute('''
    SELECT user_id, `key`, value FROM Auth_Details
''')

# fetch details and sort into dict
details = {}
for row in daiquiri_cursor.fetchall():
    user_id, key, value = row

    if user_id not in details:
        details[user_id] = {}

    if key not in ['code']:
        details[user_id][key] = value

# query all users from the daiquiri database
daiquiri_cursor.execute('''
    SELECT u.id, u.username, u.email, u.password, u.role_id, r.role, s.status
    FROM Auth_User AS u
    JOIN Auth_Roles AS r ON u.role_id = r.id
    JOIN Auth_Status AS s ON u.status_id = s.id
''')

# fetch users and create fixtures for every user, profile and email address (for allauth)
for row in daiquiri_cursor.fetchall():
    user_id, username, email, password, role_id, role, status = row

    first_name = details[user_id].pop('firstname')
    last_name = details[user_id].pop('lastname')

    is_superuser = (role == 'admin')
    is_staff = is_superuser
    is_active = (status == 'active')

    if role not in ['guest', 'user', 'admin']:
        groups = [role_id]
    else:
        groups = []

    # create a user fixture
    fixtures.append({
        'model': 'auth.user',
        'pk': user_id,
        'fields': {
            'password': 'crypt_sha512' + password,
            'last_login': None,
            'is_superuser': is_superuser,
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'is_staff': is_staff,
            'is_active': is_active,
            'date_joined': DATE_JOINED,
            'groups': groups,
            'user_permissions': []
        }
    })

    # print(details[user_id])

    # create a profile fixture
    fixtures.append({
        'model': 'daiquiri_auth.profile',
        'pk': user_id,
        'fields': {
            'user': user_id,
            'is_pending': False,
            'is_confirmed': False,
            'details': details[user_id],
            'attributes': None
        }
    })

    # create a email address fixture (for allauth)
    fixtures.append({
        'model': 'account.emailaddress',
        'pk': user_id,
        'fields': {
            'user': user_id,
            'email': email,
            'verified': True,
            'primary': True
        }
    })

print(json.dumps(fixtures, indent=2, sort_keys=True))
