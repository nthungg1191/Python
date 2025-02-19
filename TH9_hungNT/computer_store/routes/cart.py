from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from models import Order, OrderDetail, Statistics, Product
from datetime import datetime
from flask_login import login_required, current_user
from datetime import date

cart = Blueprint('cart', __name__, url_prefix='/cart')

@cart.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """ Thêm sản phẩm vào giỏ hàng """
    product = Product.get_by_id(product_id)
    if not product:
        flash("Sản phẩm không tồn tại!", "danger")
        return redirect(url_for('products.view_products'))
    
    if 'cart' not in session:
        session['cart'] = []  # Tạo giỏ hàng nếu chưa có

    # Kiểm tra nếu sản phẩm đã tồn tại trong giỏ hàng, tăng số lượng
    for item in session['cart']:
        if item['id'] == product.id:
            item['quantity'] += 1
            session.modified = True
            flash(f"Đã thêm {product.name} vào giỏ hàng!", "success")
            return redirect(url_for('products.view_products'))

    # Nếu chưa có sản phẩm trong giỏ hàng, thêm mới
    session['cart'].append({'id': product.id, 'name': product.name, 'price': product.price, 'quantity': 1})
    session.modified = True
    flash(f"Đã thêm {product.name} vào giỏ hàng!", "success")
    return redirect(url_for('products.view_products'))

@cart.route('/view')
def view_cart():
    """ Hiển thị giỏ hàng """
    return render_template('cart.html')

@cart.route('/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    """ Xóa sản phẩm khỏi giỏ hàng """
    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item['id'] != product_id]
        session.modified = True
        flash("Đã xóa sản phẩm khỏi giỏ hàng.", "success")
    return redirect(url_for('cart.view_cart'))

@cart.route('/checkout', methods=['POST'])
@login_required
def checkout():
    """ Xử lý thanh toán đơn hàng """
    if 'cart' not in session or not session['cart']:
        flash("Giỏ hàng trống!", "danger")
        return redirect(url_for('cart.view_cart'))

    total_price = sum(float(item['price']) * int(item['quantity']) for item in session['cart'])

    # ✅ Kiểm tra số lượng sản phẩm trong kho
    for item in session['cart']:
        product = Product.get_by_id(item['id'])
        if not product:
            flash(f"Sản phẩm {item['name']} không tồn tại!", "danger")
            return redirect(url_for('cart.view_cart'))
        
        if int(item['quantity']) > product.stock:
            flash(f"Sản phẩm {item['name']} chỉ còn {product.stock} cái trong kho!", "danger")
            return redirect(url_for('cart.view_cart'))

    # ✅ Tạo đơn hàng
    order_id = Order.create_order(current_user.id, total_price)

    # ✅ Lưu chi tiết đơn hàng và trừ số lượng sản phẩm
    for item in session['cart']:
        Product.update_stock(item['id'], -int(item['quantity']))  # Trừ số lượng sản phẩm
        OrderDetail.add_order_detail(order_id, item['id'], item['quantity'], item['price'])

    # ✅ Cập nhật thống kê doanh thu
    today = date.today()
    Statistics.update_statistics(today, total_price, 1, sum(int(item['quantity']) for item in session['cart']))

    # ✅ Xóa giỏ hàng sau khi thanh toán thành công
    session.pop('cart', None)
    flash("Thanh toán thành công!", "success")
    return redirect(url_for('orders.view_orders'))

@cart.route('/update_quantity/<int:product_id>', methods=['POST'])
def update_quantity(product_id):
    """ Cập nhật số lượng sản phẩm trong giỏ hàng """
    new_quantity = int(request.form['quantity'])

    if 'cart' in session:
        for item in session['cart']:
            if item['id'] == product_id:
                item['quantity'] = new_quantity
                break  # Cập nhật xong thì thoát vòng lặp
        session.modified = True
        flash("Cập nhật số lượng thành công!", "success")

    return redirect(url_for('cart.view_cart'))
