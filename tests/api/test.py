def test_api_url(set_env_vars):
    api_url = set_env_vars.get("USSP_URL")
    assert api_url == "https://localhost:8000"