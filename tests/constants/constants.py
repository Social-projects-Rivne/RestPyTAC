# Default constants


class DefaultUser:

    user = "admin"
    password = "qwerty"

    user_akimatc = "akimatc"
    user_admin = "admin"
    password_akimatc = "qwerty"
    password_admin = "qwerty"


class DefaultToken:

    token = "0123456789ABCDEF0123456789ABCDEF"


class DefaultItem:

    item = "empty"


class DefaultNum:

    num = 1000


class DefaultBool:

    bool = False


class InitUsers:

    users = {"admin": "qwerty",
             "akimatc": "qwerty",
             "khalaktc": "qwerty",
             "kilinatc": "qwerty",
             "OKonokhtc": "qwerty",
             "otlumtc": "qwerty",
             "slototc": "qwerty",
             "vbudktc": "qwerty",
             "vvasylystc": "qwerty"}


class InitFake:

    """The dictionary with fake users"""
    fake_users = {"administrator": "QWERTY",
                     "akimatc1": "qwerty",
                     "petro": "qwerty",
                     "vokodumer": "qwerty",
                     "vasya": "OKonokhtc"}

    wrong_password = 'yaroslav'


class BaseUrl:

    base_url = "http://localhost:8080"

class NewUser:
    """Constants to create new user"""

    name = "Username"
    password = "newtestpass"
    isAdmin = "true"
    isUser = "false"
    wrong_rights = "admen"

class Endpoints:

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
    locked_user = "/locked/user/"
    locked_reset = "/locked/reset"
    item_user = "/item/user"
    item = "/item/"
    items = "/items"
    itemindexes = "/itemindexes"
