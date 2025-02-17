from . import (
    QUERY_PARAM_API_KEY_NAME,
    QUERY_PARAM_INTENDED_AUDIENCE_NAME,
    QUERY_PARAM_SCOPE_NAME,
    QUERY_PARAM_SUB_NAME,
)


class AuthenticationMocks:
    INVALID_JWT_TOKEN: str = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    )

    DEFAULT_TOKEN_REQUEST_SUB: str = "icea"

    INVALID_QUERY_TOKEN_SCOPE: str = "utm.invalid_scope"

    INVALID_TOKEN_INTENDED_AUDIENCE: str = "mocked.audience"

    INVALID_TOKEN_API_KEY: str = "317672ed-767c-4db2-afea-a48a0c8383b2"

    INVALID_TOKEN_REQUEST_PARAMETER_STR: dict = {
        QUERY_PARAM_SUB_NAME: DEFAULT_TOKEN_REQUEST_SUB,
        QUERY_PARAM_SCOPE_NAME: INVALID_QUERY_TOKEN_SCOPE,
        QUERY_PARAM_INTENDED_AUDIENCE_NAME: INVALID_TOKEN_INTENDED_AUDIENCE,
        QUERY_PARAM_API_KEY_NAME: INVALID_TOKEN_API_KEY,
    }
