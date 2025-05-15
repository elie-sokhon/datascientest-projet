import re

FORBIDDEN_WORDS = {"admin", "moderator", "system"}


def is_valid_pseudonym(pseudonym: str) -> bool:
    """
    Validate pseudonym:
    - Between 3 and 15 characters
    - Only letters, numbers, underscores
    - Not in forbidden words
    """
    if not (3 <= len(pseudonym) <= 15):
        return False

    # Allow only alphanumeric + underscores
    if not re.match(r"^\w+$", pseudonym):
        return False

    # Lowercase comparison for forbidden words
    if pseudonym.lower() in FORBIDDEN_WORDS:
        return False

    return True
