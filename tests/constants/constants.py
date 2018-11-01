"""Default constants"""


ITEM_NAMES = ["Product", "Car", "Soap", "TV", "Wine", "Tea", "Coffee", "Bread", "apple", "laptop",
              "fish", "cat", "dog", "pineapple", "phone", "number1", "number2"]
VALID_STATUS_CODE = 200
INVALID_TOKEN = "2134rfvsd231g45"


class DefaultUser:
    """Default user with admin rights. Has admin token"""
    user = "admin"
    password = "qwerty"
    user_akimatc = "akimatc"
    user_admin = "admin"
    password_akimatc = "qwerty"
    password_admin = "qwerty"


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
    users = {"akimatc": "qwerty",
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


class UserToTest:
    """User to test"""
    login = "otlumtc"
    password = "qwerty"


class InvalidValues:
    """Invalid values for login and passwords"""
    values = ("qwerty ", "        ", "", "!@#$%^&*()><", "ываываыва", "ÆðÆðÆðÆð",
              "本本本本", "555555555555555555555555555555555555555555555555555555555555555555555555555555555", "k")


class BaseUrl:
    """Url for connecting to API"""
    base_url = "http://localhost:8080"

    
class InvalidUrl:
    """Invalid url for testing exceptions"""
    invalid_url = "http://localhost:80801"
    
    
class NewUser:
    """Constants to create new user"""
    name = "Username"
    password = "newtestpass"
    isAdmin = "true"
    isUser = "false"
    wrong_rights = "admen"


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
    locked_user = "/locked/user/"
    locked_reset = "/locked/reset"
    item_user = "/item/user/{name}"
    item_user_by_index = "/item/{index}/user/{name}"
    item = "/item/{index}"
    items = "/items"
    itemindexes = "/itemindexes"
