# Python imports
import re


def validate_email_address(email):
    """
    validates email address
    :param: email
    """
    if email is not None:
        # check that email is not starting with a character, has @ and . in appropriate positions
        if re.match(r'^(?![.%+-])[a-zA-Z0-9._%+-]+[a-zA-Z0-9]+@[a-zA-Z0-9]+[+-]{0,1}[a-zA-Z0-9]+\.'
                    r'[a-zA-Z]+\.{0,1}[a-zA-Z]+$', email):
            return True

    return False
