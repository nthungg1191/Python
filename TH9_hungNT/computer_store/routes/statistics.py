from flask import Blueprint, render_template

statistics = Blueprint('statistics', __name__, url_prefix='/statistics')

@statistics.route('/')
def view_statistics():
    return render_template('statistics.html')
