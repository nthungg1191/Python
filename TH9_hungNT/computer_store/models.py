import mysql.connector
from config import DATABASE_CONFIG
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Hàm kết nối CSDL MySQL
def get_db_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)

# ------------------------- User Model -------------------------
class User(UserMixin):
    def __init__(self, id, username, email, password_hash, role, created_at=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = created_at

    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        conn.close()
        if user_data:
            return User(**user_data)
        return None
    
    @staticmethod
    def get_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        conn.close()
        if user_data:
            return User(**user_data)
        return None

    @staticmethod
    def create(username, email, password):
        conn = get_db_connection()
        cursor = conn.cursor()

        # Mã hóa mật khẩu trước khi lưu vào DB
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Mặc định role là "customer"
        role = "customer"

        cursor.execute(
            "INSERT INTO users (username, email, password_hash, role) VALUES (%s, %s, %s, %s)",
            (username, email, hashed_password, role)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return [User(**user) for user in users]

    def is_admin(self):
        return self.role == "admin"
    @staticmethod
    def update_role(user_id, new_role):
        """ Cập nhật vai trò người dùng (user ↔ admin) """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET role = %s WHERE id = %s", (new_role, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(user_id):
        """ Xóa tài khoản người dùng """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        conn.close()

# ------------------------- Product Model -------------------------
class Product:
    def __init__(self, id, name, description, price, stock, image_url, created_at):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.image_url = image_url
        self.created_at = created_at

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        conn.close()
        return [Product(**product) for product in products]

    @staticmethod
    def get_by_id(product_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product_data = cursor.fetchone()
        conn.close()
        return Product(**product_data) if product_data else None

    @staticmethod
    def create(name, description, price, stock, image_url):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, description, price, stock, image_url) VALUES (%s, %s, %s, %s, %s)",
            (name, description, price, stock, image_url)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update(product_id, name, description, price, stock, image_url):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET name = %s, description = %s, price = %s, stock = %s, image_url = %s WHERE id = %s",
            (name, description, price, stock, image_url, product_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()
        conn.close()
    @staticmethod
    def update_stock(product_id, quantity_change):
        """ Cập nhật số lượng sản phẩm sau khi mua hàng """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET stock = stock + %s WHERE id = %s",
            (quantity_change, product_id)
        )
        conn.commit()
        conn.close()
        
class Order:
    def __init__(self, id, user_id, total_price, status, created_at):
        self.id = id
        self.user_id = user_id
        self.total_price = total_price
        self.status = status
        self.created_at = created_at

    @staticmethod
    def create_order(user_id, total_price):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO orders (user_id, total_price) VALUES (%s, %s)",
            (user_id, total_price)
        )
        order_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return order_id
    @staticmethod
    def get_orders_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orders WHERE user_id = %s ORDER BY created_at DESC", (user_id,))
        orders = cursor.fetchall()
        conn.close()
        return [Order(**order) for order in orders] if orders else []
    @staticmethod
    def get_all_orders():
        """Lấy tất cả đơn hàng (Admin)"""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orders ORDER BY created_at DESC")
        orders = cursor.fetchall()
        conn.close()
        return [Order(**order) for order in orders] if orders else []
    
    @staticmethod
    def update_order_status(order_id, new_status):
        """Cập nhật trạng thái đơn hàng"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE orders SET status = %s WHERE id = %s",
            (new_status, order_id)
        )
        conn.commit()
        conn.close()



# ------------------------- Order Details Model -------------------------
class OrderDetail:
    def __init__(self, id, order_id, product_id, quantity, price):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    @staticmethod
    def add_order_detail(order_id, product_id, quantity, price):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
            (order_id, product_id, quantity, price)
        )
        conn.commit()
        conn.close()


# ------------------------- Statistics Model -------------------------
from datetime import datetime

class Statistics:
    @staticmethod
    def get_today_statistics():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # ✅ Chỉ tính doanh thu từ đơn hàng "completed"
        cursor.execute("""
            SELECT 
                COALESCE(SUM(total_price), 0) AS total_revenue,
                COUNT(id) AS total_orders,
                SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed_orders,
                SUM(CASE WHEN status = 'canceled' THEN 1 ELSE 0 END) AS canceled_orders,
                COALESCE(SUM((SELECT SUM(quantity) FROM order_details WHERE order_id = orders.id)), 0) AS total_products_sold
            FROM orders
            WHERE DATE(created_at) = CURDATE()
        """)
        today_stats = cursor.fetchone()
        conn.close()

        return today_stats
    
    @staticmethod
    def get_monthly_statistics():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # ✅ Chỉ tính doanh thu từ đơn hàng "completed"
        cursor.execute("""
            SELECT 
                COALESCE(SUM(total_price), 0) AS total_revenue,
                COUNT(id) AS total_orders,
                SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed_orders,
                SUM(CASE WHEN status = 'canceled' THEN 1 ELSE 0 END) AS canceled_orders,
                COALESCE(SUM((SELECT SUM(quantity) FROM order_details WHERE order_id = orders.id)), 0) AS total_products_sold
            FROM orders
            WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())
        """)
        monthly_stats = cursor.fetchone()
        conn.close()

        return monthly_stats
    
    @staticmethod
    def update_statistics(date, revenue, total_orders, total_products_sold):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO statistics (report_date, total_revenue, total_orders, total_products_sold)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            total_revenue = total_revenue + %s,
            total_orders = total_orders + %s,
            total_products_sold = total_products_sold + %s
            """,
            (date, revenue, total_orders, total_products_sold, revenue, total_orders, total_products_sold)
        )
        conn.commit()
        conn.close()


