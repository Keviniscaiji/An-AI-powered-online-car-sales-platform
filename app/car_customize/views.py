from flask import render_template, session, redirect, url_for
from flask_login import current_user

from app import db
from . import car_customize
from ..models import Cart, Product


@car_customize.route('/car_customize')
def index():
    return render_template('car_customize/index.html')


from flask import request, jsonify


@car_customize.route('/car_customize', methods=['POST'])
def handle_colors():
    data = request.get_json()
    car_color = data.get('carColor')
    carType = data.get('carType')
    product = Product.query.filter_by(name=carType).first()
    item = Cart(
        customized_color=car_color,
        count=1,
        is_selected=True,
        owner_id=current_user.id,
        product_id=product.id
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({'status': 'success'})
