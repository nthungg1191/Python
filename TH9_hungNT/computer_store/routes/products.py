from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Product
from flask_login import login_required
from utils import admin_required

# Blueprint cho sản phẩm
products = Blueprint('products', __name__, url_prefix='/products')

# Xem danh sách sản phẩm
@products.route('/')
def view_products():
    products_list = Product.get_all()  # Lấy tất cả sản phẩm
    return render_template('products_list.html', products=products_list)

# Thêm sản phẩm
@products.route('/product/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description'].strip()  # Lấy mô tả, loại bỏ khoảng trắng
        price = request.form['price']
        stock = request.form['stock']
        image_url = request.form['image_url']

        # ✅ Nếu mô tả bị trống, gán giá trị mặc định
        if not description:
            description = "Chưa có mô tả cho sản phẩm này"

        # ✅ Lưu vào database
        Product.create(name, description, price, stock, image_url)
        flash('Thêm sản phẩm thành công!', 'success')
        return redirect(url_for('products.view_products'))

    return render_template('add_product.html')



# Sửa sản phẩm
@products.route('/product/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        flash("Sản phẩm không tồn tại", "danger")
        return redirect(url_for('products.view_products'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        image_url = request.form['image_url']
        Product.update(product_id, name, description, price, stock, image_url)
        flash('Cập nhật sản phẩm thành công!', 'success')
        return redirect(url_for('products.view_products'))

    
    return render_template('edit_product.html', product=product)



# Xóa sản phẩm
@products.route('/product/delete/<int:product_id>', methods=['POST'])
@login_required
@admin_required
def delete_product(product_id):
    Product.delete(product_id)
    flash("Xóa sản phẩm thành công!", "success")
    return redirect(url_for('products.view_products'))



# Chi tiết sản phẩm
@products.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        flash("Sản phẩm không tồn tại", "danger")
        return redirect(url_for('products.view_products'))
    return render_template('product_detail.html', product=product)
