LEGACY_DATABASE = {
    'db': 'daiquiri_web',
    'user': '',
    'password': '',
    'host': '',
    'port': 3306
}

DJANGO_DATABASE = {
    'db': 'daiquiri_app',
    'user': '',
    'password': '',
    'host': '',
    'port': 3306
}

WORDPRESS_DATABASE = {
    'db': 'daiquiri_wp',
    'user': '',
    'password': '',
    'host': '',
    'port': 3306
}

# custom user detail keys
AUTH_DETAIL_KEYS = ['affiliation']

# date to be used as date_joined for all users
DATE_JOINED = '2018-04-01T00:00:00Z'

# date to be used for contact messages without a date
DEFAULT_CONTRACT_MESSAGE_DATE = '2015-01-01'

# query language for the query examples
QUERY_EXAMPLE_LANGUAGE = 'mysql'

# query language for the query jobs
QUERY_JOB_LANGUAGE = 'postgresql'

# map status -> phase (direct query)
# QUERY_JOB_PHASES = {
#     1: 'COMPLETED',  # success
#     2: 'ERROR',      # timeout
#     3: 'ARCHIVED'    # removed
# }

# map status -> phase (qqueue)
# QUERY_JOB_PHASES = {
#     0: 'QUEUED',     # queued
#     1: 'EXECUTING',  # running
#     2: 'ARCHIVED',   # removed
#     3: 'ERROR',      # error
#     4: 'COMPLETED',  # success
#     5: 'ERROR',      # timeout
#     6: 'ABORT'       # killed
# }

# map type_id -> job_type
QUERY_JOB_TYPES = {
    1: 'INTERFACE',  # web
    2: 'ASYNC'       # uws
}

# replacements for the user schema
QUERY_USER_SCHEMA_REPLACEMENTS = (
    ('foo_user_', 'bar_user_'),
)

# replacements for the query string
QUERY_STRING_REPLACEMENTS = (
    ('`', '"'),
    ('log10', 'log'),
)
