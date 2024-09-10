from collections.abc import Collection
from typing import Any
from typing_extensions import TypeAlias

from ... import OAuth2Request
from .. import ClientMixin
from .base import AuthorizationEndpointMixin, BaseGrant, TokenEndpointMixin

_SERVER_RESPONSE: TypeAlias = tuple[int, str, list[tuple[str, str]]]

class AuthorizationCodeGrant(BaseGrant, AuthorizationEndpointMixin, TokenEndpointMixin):
    TOKEN_ENDPOINT_AUTH_METHODS: Collection[str]
    AUTHORIZATION_CODE_LENGTH: int
    RESPONSE_TYPES: Collection[str]
    GRANT_TYPE: str
    def validate_authorization_request(self) -> str: ...
    def create_authorization_response(self, redirect_uri: str, grant_user: Any) -> _SERVER_RESPONSE: ...
    def validate_token_request(self) -> None: ...
    def create_token_response(self) -> _SERVER_RESPONSE: ...
    def generate_authorization_code(self) -> str: ...
    def save_authorization_code(self, code: str, request: OAuth2Request) -> None: ...
    def query_authorization_code(self, code: str, client: ClientMixin) -> Any: ...
    def delete_authorization_code(self, authorization_code: Any) -> None: ...
    def authenticate_user(self, authorization_code: Any) -> Any: ...

def validate_code_authorization_request(grant: AuthorizationCodeGrant) -> str: ...
