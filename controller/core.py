from functools import wraps

from flask  import session as login_session, redirect, url_for

# user login decorator


def user_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'username' in login_session:
            return redirect(url_for('user.login'))
        return f(*args, **kwargs)
    return decorator