class AuthenticationMocks:
    INVALID_JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

    INVALID_AUTH_PARAMETERS = {
        "scope": "utm.invalid_scope",
        "intended_audience": "mocked.audience",
        "apikey": "317672ed-767c-4db2-afea-a48a0c8383b2",
    }
