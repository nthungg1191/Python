from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from models import User, bcrypt
from flask_bcrypt import Bcrypt
import mysql.connector
from config import DATABASE_CONFIG
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


def get_db_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)

auth = Blueprint('auth', __name__)

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    user = User.get_by_username(user_id)
    return user if user else None

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Kiểm tra xem username có tồn tại trong hệ thống không
        user = User.get_by_username(username)
        if user and check_password_hash(user.password_hash, password):

            # Nếu thông tin đúng, đăng nhập vào hệ thống
            login_user(user)
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('main_routes.home'))
        else:
            # Nếu thông tin sai, hiển thị thông báo lỗi
            flash('Sai tên đăng nhập hoặc mật khẩu!', 'danger')
    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Kiểm tra xem username đã tồn tại chưa
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash('Tên người dùng đã tồn tại!', 'danger')
        else:
            # Mã hóa mật khẩu
            hashed_password = generate_password_hash(password)
            
            # Tạo tài khoản mới
            cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                           (username, email, hashed_password))
            conn.commit()
            flash('Đăng ký thành công! Hãy đăng nhập.', 'success')
            
            cursor.close()
            conn.close()
            return redirect(url_for('auth.login'))
        
        cursor.close()
        conn.close()
    
    return render_template('register.html')
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bạn đã đăng xuất!', 'info')
    return redirect(url_for('home'))
