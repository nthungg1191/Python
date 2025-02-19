from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import logout_user, login_required

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html')

@main_routes.route('/login')
def login():
    return render_template('login.html')

@main_routes.route('/register')
def register():
    return render_template('register.html')

@main_routes.route('/statistics')
def statistics():
    return render_template('statistics.html')

@main_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Đăng xuất thành công!', 'info')
    return redirect(url_for('main_routes.home'))  # Sử dụng `main_routes.home`
