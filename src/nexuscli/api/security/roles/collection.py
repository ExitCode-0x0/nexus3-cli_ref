import json
from typing import List, Optional

from nexuscli.api import util
from nexuscli.api.base_collection import BaseCollection
from nexuscli.api.security.roles.model import Role

class RoleCollection(BaseCollection):
    def __init__(self, client):
        super().__init__(client)
    
    @util.with_min_version('3.68.1')
    def raw_list(self) -> List[Role]:
        # Implement the logic to retrieve roles from Nexus using the raw list method
        return self._http.service_get('security/roles')
    
    @util.with_min_version('3.68.1')
    def show(self, role_id: str) -> Role:
        # Implement the logic to retrieve a specific role by ID from Nexus using the show method
        return self._http.service_get(f'security/roles/{role_id}')
    
    @util.with_min_version('3.68.1')
    def create(self, data: dict) -> Role:
        # Implement the logic to create a new role in Nexus using the create method
        response = self._http.service_post('security/roles', json=data)
        return Role.from_json(response.json())
    
    @util.with_min_version('3.68.1')
    def delete(self, role_id: str) -> None:
        # Implement the logic to delete a specific role by ID from Nexus using the delete method
        resp = self._http.service_delete(f'security/roles/{role_id}')
        util.validate_response(resp, [201],[204])
        self.reset()
    
    @util.with_min_version('3.68.1')
    def update(self, role_id: str, data: dict) -> Role:
        # Implement the logic to update a specific role by ID in Nexus using the update method
        response = self._http.service_put(f'security/roles/{role_id}', json=data)
        return Role.from_json(response.json())
    