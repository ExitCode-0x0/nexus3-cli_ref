import json
from texttable import Texttable

from nexuscli import exception
from nexuscli.cli import constants
from nexuscli import NexusClient

def cmd_list(nexus_client):
    """Perform `nexus3 security role list`."""
    roles = nexus_client.security_roles.list()
    
    table = Texttable(max_width=constants.TTY_MAX_WIDTH)
    table.add_row(['ID', 'Source', 'Name', 'Description', 'Read Only'])
    for role in roles:
        table.add_row([role['id'], role['source'], role['name'], role['description'], role['readOnly']])
    print(table.draw())
    return exception.CliReturnCode.SUCCESS.value

def cmd_show(nexus_client, role_id):
    """Perform `nexus3 security role show`."""
    try:
        role = nexus_client.security_roles.show(role_id)
        print(json.dumps(role, indent=4))
    except Exception as e:
        raise exception.CliReturnCode.FAILURE.value from e

def cmd_create(nexus_client, name, description):
    """Perform `nexus3 security role create`."""
    try:
        role = nexus_client.security_roles.create(name=name, description=description)
        print(json.dumps(role, indent=4))
    except Exception as e:
        raise exception.CliReturnCode.FAILURE.value from e

def cmd_delete(nexus_client, role_id):
    """Perform `nexus3 security role delete`."""
    try:
        nexus_client.security_roles.delete(role_id)
        print(f"Role {role_id} deleted successfully.")
    except Exception as e:
        raise exception.CliReturnCode.FAILURE.value from e

def cmd_update(nexus_client, role_id, name=None, description=None):
    """Perform `nexus3 security role update`."""
    try:
        updated_role = nexus_client.security_roles.update(role_id, name=name, description=description)
        print(json.dumps(updated_role, indent=4))
    except Exception as e:
        raise exception.CliReturnCode.FAILURE.value from e
