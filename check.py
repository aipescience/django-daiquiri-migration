#!/usr/bin/env python

import MySQLdb
import settings

# get a connection to the legacy database
legacy_connection = MySQLdb.connect(**settings.LEGACY_DATABASE)
legacy_cursor = legacy_connection.cursor()
legacy_cursor.execute('SELECT count(*) FROM Auth_User')
legacy_count = legacy_cursor.fetchone()

if legacy_count is None:
    print('No connection to LEGACY_DATABASE.')
else:
    print('Connection to LEGACY_DATABASE works! Found %d users.' % legacy_count)

# get a connection to the daiquiri database
django_connection = MySQLdb.connect(**settings.DJANGO_DATABASE)
django_cursor = django_connection.cursor()
django_cursor.execute('SELECT count(*) FROM auth_user')
django_count = django_cursor.fetchone()

if django_count is None:
    print('No connection to DJANGO_DATABASE.')
else:
    print('Connection to DJANGO_DATABASE works! Found %d users.' % django_count)

# get a connection to the wordpres database
wordpress_connection = MySQLdb.connect(**settings.WORDPRESS_DATABASE)
wordpress_cursor = wordpress_connection.cursor()
wordpress_cursor.execute('SELECT count(*) FROM wp_users');
wordpress_count = wordpress_cursor.fetchone()

if wordpress_count is None:
    print('No connection to WORDPRESS_DATABASE.')
else:
    print('Connection to WORDPRESS_DATABASE works! Found %d users.' % wordpress_count)
