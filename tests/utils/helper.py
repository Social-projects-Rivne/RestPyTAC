from tests.constants.constants import BaseUrl


def generate_full_url(path):
    return "{}{}".format(BaseUrl.base_url, path)
