# Default constants


class DefaultUser:
    user = "admin"
    password = "qwerty"


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


class InitInvalidUsers:
    invalid_users = {"admin": "QWERTY",
                     "akimatc1": "qwerty",
                     "khalaktc": "",
                     "": "qwerty",
                     "OKonokhtc": "OKonokhtc"}


class UserToTest:
    """User to test"""

    login = "otlumtc"
    password = "qwerty"


class NewUser:
    """Constants to create new user"""

    name = "Username"
    password = "newtestpass"
    isAdmin = "true"
    isUser = "false"
    wrong_rights = "admen"


class InvalidValues:
    """Invalid values for login and passwords"""

    values = {
        0: "qwerty ",
        1: "        ",
        2: "",
        3: "!@#$%^&*()><",
        4: "ываываыва",
        5: "ÆðÆðÆðÆð",
        6: "本本本本",
        7: "5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"
           "55555555555555555555555555555555555555555555555555555555555555555555",
        8: "k"
    }


class BaseUrl:
    base_url = "http://localhost:8080"


class InvalidUrl:
    invalid_url = "http://localhost:80801"


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
    locked_user = "/locked/user"
    locked_reset = "/locked/reset"
    item_user = "/item/user"
    item = "/item"
    items = "/items"
    itemindexes = "/itemindexes"
