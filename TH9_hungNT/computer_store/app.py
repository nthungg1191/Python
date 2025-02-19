from flask import Flask, render_template
from routes.main_routes import main_routes
from flask_login import LoginManager
from auth import auth, login_manager
from models import get_db_connection
from models import User
from routes import products, users, statistics  # Import các blueprint
from routes.products import products
from routes.cart import cart
from routes.orders import orders
from routes.admin import admin


app = Flask(__name__, template_folder="templates")

app = Flask(__name__)
app.register_blueprint(admin)
app.register_blueprint(cart)
app.register_blueprint(main_routes)
app.register_blueprint(products)
app.register_blueprint(orders)
app.register_blueprint(users)
app.register_blueprint(statistics)
app.config.from_object('config')
app.secret_key = 'secret_key'

app.register_blueprint(auth)
login_manager = LoginManager()
login_manager.init_app(app)
# Khởi tạo các route

@login_manager.user_loader
def load_user(user_id):
    # Trả về đối tượng người dùng từ database theo user_id
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        return User(**user_data)  # Tạo đối tượng User từ dữ liệu trong DB
    return None

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

if __name__ == '__main__':
    app.run(debug=True)

