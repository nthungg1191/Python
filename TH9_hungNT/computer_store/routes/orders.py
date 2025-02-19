from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Order

orders = Blueprint('orders', __name__, url_prefix='/orders')

@orders.route('/view')
@login_required
def view_orders():
    """ Hiển thị danh sách đơn hàng của người dùng """
    print(f"DEBUG: current_user.id = {current_user.id}")  # Kiểm tra giá trị user ID
    user_orders = Order.get_orders_by_user(current_user.id)  # Gọi đúng phương thức đã sửa
    return render_template('orders.html', orders=user_orders)

    

