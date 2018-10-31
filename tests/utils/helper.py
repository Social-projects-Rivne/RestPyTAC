"""Help functions for testing"""

from tests.constants.constants import BaseUrl


def generate_full_url(path):
    """Generate the full url with base url and path"""
    return "{}{}".format(BaseUrl.base_url, path)
