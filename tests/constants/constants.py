"""Default constants"""


class DefaultUser:
    """Default user with admin rights. Has admin token"""
    user = "admin"
    password = "qwerty"


class Users:
    """Default valid user, password and fake user, password"""
    valid_user = "vvasylystc"
    valid_password = "qwerty"
    fake_user = "vVASYLystc333"
    fake_password = "Qwerty123"


class DefaultToken:
    """Default token"""
    token = "0123456789ABCDEF0123456789ABCDEF"


class DefaultItem:
    """Default item for items"""
    item = "empty"


class DefaultNum:
    """Default number for items"""
    num = 1000


class DefaultBool:
    """Default bool for items"""
    bool = False


class InitUsers:
    """The dictionary of all valid users"""
    users = {"admin": "qwerty",
             "akimatc": "qwerty",
             "khalaktc": "qwerty",
             "kilinatc": "qwerty",
             "OKonokhtc": "qwerty",
             "otlumtc": "qwerty",
             "slototc": "qwerty",
             "vbudktc": "qwerty",
             "vvasylystc": "qwerty"}


class InitInvalidUsers:
    """The dictionary with fake users"""
    invalid_users = {"admin": "QWERTY",
                     "akimatc1": "qwerty",
                     "khalaktc": "",
                     "": "qwerty",
                     "OKonokhtc": "OKonokhtc"}


class BaseUrl:
    """Url for connecting to API"""
    base_url = "http://localhost:8080"


class InvalidUrl:
    """Invalid url for testing exceptions"""
    invalid_url = "http://localhost:80801"


class Endpoints:
    """All endpoints in API"""
    reset = "/reset"
    login = "/login"
    logout = "/logout"
    user = "/user"
    cooldowntime = "/cooldowntime"
    tokenlifetime = "/tokenlifetime"
    admins = "/admins"
    login_admins = "/login/admins"
    locked_admins = "/locked/admins"
    users = "/users"
    login_users = "/login/users"
    login_tockens = "/login/tockens"
    locked_users = "/locked/users"
    locked_user = "/locked/user"
    locked_reset = "/locked/reset"
    item_user = "/item/user"
    item = "/item"
    items = "/items"
    itemindexes = "/itemindexes"
