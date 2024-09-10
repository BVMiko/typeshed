from _typeshed import Incomplete

from authlib.oauth2.rfc6749 import AuthorizationCodeMixin, TokenMixin

class OAuth2AuthorizationCodeMixin(AuthorizationCodeMixin):
    code: Incomplete
    client_id: Incomplete
    redirect_uri: Incomplete
    response_type: Incomplete
    scope: Incomplete
    nonce: Incomplete
    auth_time: Incomplete
    code_challenge: Incomplete
    code_challenge_method: Incomplete
    def is_expired(self): ...
    def get_redirect_uri(self): ...
    def get_scope(self): ...
    def get_auth_time(self): ...
    def get_nonce(self): ...

class OAuth2TokenMixin(TokenMixin):
    client_id: Incomplete
    token_type: Incomplete
    access_token: Incomplete
    refresh_token: Incomplete
    scope: Incomplete
    issued_at: Incomplete
    access_token_revoked_at: Incomplete
    refresh_token_revoked_at: Incomplete
    expires_in: Incomplete
    def check_client(self, client): ...
    def get_scope(self): ...
    def get_expires_in(self): ...
    def is_revoked(self): ...
    def is_expired(self): ...
