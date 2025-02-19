from flask import redirect, url_for, flash
from flask_login import current_user
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash("Bạn không có quyền truy cập vào trang này!", "danger")
            return redirect(url_for('main_routes.home'))
        return f(*args, **kwargs)
    return decorated_function
