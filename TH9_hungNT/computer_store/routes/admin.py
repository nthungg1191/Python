from flask import Blueprint, render_template, redirect, url_for, request, flash, send_file, current_app
from flask_login import login_required, current_user
from models import Order, Statistics, User
from utils import admin_required  # Middleware kiểm tra quyền admin
import openpyxl
import datetime
import time
import os

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/orders')
@login_required
@admin_required  # Chỉ admin mới có quyền
def manage_orders():
    """ Hiển thị danh sách đơn hàng cho Admin """
    orders = Order.get_all_orders()
    return render_template('admin_orders.html', orders=orders)

@admin.route('/orders/update/<int:order_id>', methods=['POST'])
@login_required
@admin_required  # Chỉ admin mới có quyền
def update_order_status(order_id):
    """ Admin cập nhật trạng thái đơn hàng """
    new_status = request.form['new_status']
    Order.update_order_status(order_id, new_status)
    flash(f"Đã cập nhật trạng thái đơn hàng #{order_id} thành {new_status}.", "success")
    return redirect(url_for('admin.manage_orders'))


@admin.route('/statistics')
@login_required
@admin_required
def view_statistics():
    """ Trang thống kê cho Admin """
    today_stats = Statistics.get_today_statistics()
    monthly_stats = Statistics.get_monthly_statistics()
    return render_template('admin_statistics.html', today_stats=today_stats, monthly_stats=monthly_stats)


@admin.route('/export-statistics')
@login_required
@admin_required
def export_statistics():
    """ Xuất thống kê ra file Excel """
    today_stats = Statistics.get_today_statistics()
    monthly_stats = Statistics.get_monthly_statistics()

    # ✅ Lấy đường dẫn tuyệt đối của thư mục static/reports
    report_dir = os.path.join(current_app.root_path, "static", "reports")
    os.makedirs(report_dir, exist_ok=True)

    # ✅ Định dạng tên file chính xác
    filename = f"statistics_{datetime.date.today()}.xlsx"
    filepath = os.path.join(report_dir, filename)

    print(f"🛠 Debug: Đường dẫn đầy đủ của file - {filepath}")

    # ✅ Xóa file cũ nếu tồn tại (tránh lỗi mở file)
    if os.path.exists(filepath):
        os.remove(filepath)

    # ✅ Tạo workbook mới
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Thống kê doanh thu"

    # ✅ Ghi dữ liệu
    ws.append(["📊 Thống kê Doanh Thu"])
    ws.append([])

    # ✅ Ghi dữ liệu thống kê hôm nay
    ws.append(["📅 Thống kê Hôm Nay"])
    ws.append(["Doanh thu", "Tổng đơn hàng", "Đơn hoàn thành", "Đơn hủy", "Sản phẩm đã bán"])
    ws.append([
        today_stats.get('total_revenue', 0),
        today_stats.get('total_orders', 0),
        today_stats.get('completed_orders', 0),
        today_stats.get('canceled_orders', 0),
        today_stats.get('total_products_sold', 0)
    ])
    ws.append([])

    # ✅ Ghi dữ liệu thống kê tháng này
    ws.append(["📅 Thống kê Tháng Này"])
    ws.append(["Doanh thu", "Tổng đơn hàng", "Đơn hoàn thành", "Đơn hủy", "Sản phẩm đã bán"])
    ws.append([
        monthly_stats.get('total_revenue', 0),
        monthly_stats.get('total_orders', 0),
        monthly_stats.get('completed_orders', 0),
        monthly_stats.get('canceled_orders', 0),
        monthly_stats.get('total_products_sold', 0)
    ])

    # ✅ Lưu file Excel
    try:
        wb.save(filepath)
        wb.close()  # Đảm bảo file không bị khóa
        print(f"✅ File đã được lưu: {filepath}")

    except Exception as e:
        print(f"❌ Lỗi khi lưu file: {e}")
        flash("❌ Xuất file thất bại, vui lòng thử lại!", "danger")
        return redirect(url_for('admin.view_statistics'))

    # ✅ Chờ hệ thống nhận diện file
    time.sleep(0.5)

    # ✅ Kiểm tra file có tồn tại không trước khi gửi
    if not os.path.exists(filepath):
        print(f"⚠️ File {filepath} không tồn tại sau khi lưu!")
        flash("❌ Lỗi khi xuất file, vui lòng thử lại!", "danger")
        return redirect(url_for('admin.view_statistics'))

    print(f"📂 Đang gửi file: {filepath}")

    flash("✅ Đã xuất thống kê ra file Excel!", "success")
    return send_file(filepath, as_attachment=True)

@admin.route('/users')
@login_required
@admin_required
def manage_users():
    """ Hiển thị danh sách tài khoản người dùng """
    users = User.get_all()
    return render_template('admin_users.html', users=users)

@admin.route('/users/update/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def update_user_role(user_id):
    """ Cập nhật vai trò người dùng (user ↔ admin) """
    new_role = request.form['new_role']
    User.update_role(user_id, new_role)
    flash(f"Đã cập nhật vai trò của người dùng #{user_id} thành {new_role}.", "success")
    return redirect(url_for('admin.manage_users'))

@admin.route('/users/delete/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    """ Xóa tài khoản người dùng """
    User.delete(user_id)
    flash(f"Đã xóa tài khoản #{user_id}.", "success")
    return redirect(url_for('admin.manage_users'))
