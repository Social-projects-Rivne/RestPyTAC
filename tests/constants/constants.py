# Default constants


class DefaultUser:

    user = "admin"
    password = "qwerty"


class DefaultToken:

    token = "0123456789ABCDEF0123456789ABCDEF"


INVALID_TOKEN = "2134rfvsd231g45"


class DefaultItem:

    item = "empty"


class DefaultNum:

    num = 1000


VALID_STATUS_CODE = 200


class DefaultBool:

    bool = False


class InitUsers:

    users = {"akimatc": "qwerty",
             "khalaktc": "qwerty",
             "kilinatc": "qwerty",
             "OKonokhtc": "qwerty",
             "otlumtc": "qwerty",
             "slototc": "qwerty",
             "vbudktc": "qwerty",
             "vvasylystc": "qwerty"}


class BaseUrl:

    base_url = "http://localhost:8080"


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
    item_user = "/item/user/{name}"
    item_user_by_index = "/item/{index}/user/{name}"
    item = "/item/{index}"
    items = "/items"
    itemindexes = "/itemindexes"


ITEM_NAMES = ["Product", "Car", "Soap", "TV", "Wine", "Tea", "Coffee", "Bread", "apple", "laptop",
              "fish", "cat", "dog", "pineapple", "phone", "number1", "number2"]
