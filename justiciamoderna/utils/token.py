""" Token funcion JWT"""
# Utils
import datetime,jwt


def is_valid_token(token):
    try:
        jwt.decode(token, 'secret_key$', algorithm=['HS256'])
    except (jwt.ExpiredSignatureError,
            jwt.DecodeError,
            jwt.InvalidTokenError):
        return False
    return True