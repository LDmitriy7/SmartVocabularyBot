"""Various functions"""
from fake_headers.headers import make_header
from fake_useragent import UserAgent


def make_headers():
    """Make fake headers"""
    headers = make_header()
    headers['user-agent'] = UserAgent().chrome
    return headers
