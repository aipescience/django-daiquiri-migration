DAIQUIRI_DATABASE = {
    'db': '',
    'user': '',
    'host': '',
    'read_default_file': '~/.my.cnf'
}

WORDPRESS_DATABASE = {
    'db': '',
    'user': '',
    'host': '',
    'read_default_file': '~/.my.cnf'
}

# date to be used as date_joined for all users
DATE_JOINED = '2018-04-01T00:00:00Z'

# query language for the query examples
QUERY_EXAMPLE_LANGUAGE = 'mysql'

# query language for the query jobs
QUERY_JOB_LANGUAGE = 'postgresql'

# map status -> phase (direct query)
QUERY_PHASES = {
    1: 'COMPLETED',  # success
    2: 'ERROR',      # timeout
    3: 'ARCHIVED'    # removed
}

# map status -> phase (qqueue)
QUERY_PHASES = {
    0: 'QUEUED',     # queued
    1: 'EXECUTING',  # running
    2: 'ARCHIVED',   # removed
    3: 'ERROR',      # error
    4: 'COMPLETED',  # success
    5: 'ERROR',      # timeout
    6: 'ABORT'       # killed
}

# prefix for the user schema
QUERY_USER_SCHEMA_PREFIX = 'gaia_user_'

# map type_id -> job_type
QUERY_TYPES = {
    1: 'INTERFACE',  # web
    2: 'ASYNC'       # uws
}
