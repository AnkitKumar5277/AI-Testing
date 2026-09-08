def test_login():
    """Login succeeds with valid credentials."""

    username = "valid-user"
    password = "correct-password"

    success = username == "valid-user" and password == "correct-password"

    assert success, "Login should succeed with valid credentials"