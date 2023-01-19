class NoSiteException(Exception):
    message = "No 'site' value on payload"

class NoPasswordException(Exception):
    message = "No 'password' value on payload"

class MaxSizeException(Exception):
    message = "The text can not have more than 50 chars"