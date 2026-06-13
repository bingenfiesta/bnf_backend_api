from src.core import validators


def test_validate_contact_number_valid():
    assert validators.validate_contact_number(9876543210) is True


def test_validate_contact_number_invalid():
    assert validators.validate_contact_number(123) is False


def test_validate_email_valid():
    assert validators.validate_email('user@example.com') is True


def test_validate_email_invalid():
    assert validators.validate_email('not-an-email') is False


def test_validate_whole_number():
    assert validators.validate_whole_number(5) is True
    assert validators.validate_whole_number(0) is False
