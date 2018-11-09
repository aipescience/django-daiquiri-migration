#!/usr/bin/env python

import MySQLdb

import settings

# fetch user from daiquiri
daiquiri_connection = MySQLdb.connect(**settings.DJANGO_DATABASE)

daiquiri_cursor = daiquiri_connection.cursor()
daiquiri_cursor.execute('SELECT id, username, first_name, last_name, email FROM auth_user;')

daiquiri_users = daiquiri_cursor.fetchall()

# update users in the wordpress database
wordpress_connection = MySQLdb.connect(**settings.WORDPRESS_DATABASE)

wordpress_cursor = wordpress_connection.cursor()
wordpress_cursor.execute('SELECT id, user_login FROM wp_users');

wordpress_users = wordpress_cursor.fetchall()

for daiquiri_id, username, first_name, last_name, email in daiquiri_users:
    for wordpress_id, wordpress_login in wordpress_users:
        if daiquiri_id == int(wordpress_login):
            display_name = '%s %s' % (first_name, last_name)
            wordpress_cursor.execute('UPDATE wp_users SET user_login = %s WHERE id = %s', (username, wordpress_id))
            wordpress_cursor.execute('UPDATE wp_users SET user_nicename = %s WHERE id = %s', (username, wordpress_id))
            wordpress_cursor.execute('UPDATE wp_users SET display_name = %s WHERE id = %s', (display_name, wordpress_id))
            wordpress_cursor.execute('UPDATE wp_users SET user_email = %s WHERE id = %s', (email, wordpress_id))

wordpress_connection.commit()
