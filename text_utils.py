"""."""
import re


def define_lang(word):
    """Recognize russian/english language or return False"""
    if re.match(r'[a-z]', word):
        return 'английский-русский'
    elif re.match(r'[а-я]', word):
        return 'русский-английский'
    return False


def match_with(*strings: str, regexp: str = None):
    """Return func that checks if lower text of given message match one of strings or regexp."""
    if regexp:
        return lambda msg: re.fullmatch(regexp, msg.text.lower())
    return lambda msg: msg.text.lower() in set(strings)
