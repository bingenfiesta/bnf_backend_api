import re


def validate_contact_number(contact_number: int):
    """Validate phone number to be 10 digit only and should be an integer."""
    if contact_number >= 1000000000 and contact_number <= 9999999999:
        return True
    return False

def validate_email(email_id: str):
    """Validate Email using Regex."""
    email_regex = "[^@]+@[^@]+\.[^@]+"
    if re.match(email_regex, email_id):
        return True
    return False

def validate_whole_number(number: int):
    return True if number > 0 else False