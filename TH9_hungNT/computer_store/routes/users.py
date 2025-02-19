from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from models import User

# Blueprint cho người dùng
users = Blueprint('users', __name__, url_prefix='/users')

# Đăng nhập
@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lấy thông tin đăng nhập từ form
        username = request.form['username']
        password = request.form['password']
        user = User.get_by_username(username)
        if user and user.verify_password(password):
            login_user(user)
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng', 'danger')
    return render_template('login.html')

# Đăng ký
@users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Thực hiện thêm người dùng vào database
        if User.create(username, password, email):
            flash('Đăng ký thành công!', 'success')
            return redirect(url_for('users.login'))
        else:
            flash('Lỗi đăng ký, vui lòng thử lại', 'danger')
    return render_template('register.html')

# Đăng xuất
@users.route('/logout')
def logout():
    logout_user()
    flash('Đăng xuất thành công!', 'info')
    return redirect(url_for('home'))

@users.route('/')
def view_users():
    return render_template('users_list.html')
