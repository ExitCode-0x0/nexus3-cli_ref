import shutil

ENV_VAR_PREFIX = 'NEXUS3'
TTY_MAX_WIDTH = shutil.get_terminal_size().columns

# see cli.util.get_client()
NEXUS_OPTIONS_FOR_LOGIN = ['PASSWORD', 'USERNAME', 'URL']
OPTIONAL_NEXUS_OPTIONS = ['API_VERSION']
BOOL_OPTIONAL_NEXUS_OPTIONS = ['GROOVY_ENABLED', 'X509_VERIFY']
