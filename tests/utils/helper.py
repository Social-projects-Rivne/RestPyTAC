from tests.constants.constants import BaseUrl


def generate_full_url(path):
    return "{}{}".format(BaseUrl.base_url, path)


def get_new_value_different_func(func, new_value, step):
    """
    Get new value which is different from returned function value.
    The function compare returned func() value and new_value (parameters).
    If they are equal then new_value increases by step.
    The function return either new_value or new_value + step
    """

    resp = func()
    func_value = resp.json()["content"]

    return new_value + step if func_value == new_value else new_value
