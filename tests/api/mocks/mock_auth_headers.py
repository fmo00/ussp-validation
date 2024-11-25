class AuthenticationMocks:
    INVALID_JWT_TOKEN: str = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    )

    DEFAULT_TOKEN_REQUEST_SUB: str = "?sub=icea"

    INVALID_QUERY_TOKEN_SCOPE: str = "&scope=utm.invalid_scope"

    INVALID_TOKEN_INTENDED_AUDIENCE: str = "&intended_audience=mocked.audience"

    INVALID_TOKEN_API_KEY: str = "&apikey=317672ed-767c-4db2-afea-a48a0c8383b2"

    INVALID_TOKEN_REQUEST_PARAMETER_STR: str = (
        DEFAULT_TOKEN_REQUEST_SUB
        + INVALID_QUERY_TOKEN_SCOPE
        + INVALID_TOKEN_INTENDED_AUDIENCE
        + INVALID_TOKEN_API_KEY
    )
