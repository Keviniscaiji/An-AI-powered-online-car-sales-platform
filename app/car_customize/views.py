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
    print(car_color, carType)
    type_dict = {
        "911": "Porsche 911", 
        "Infiniti": "Infiniti Project Black S", 
        "old911": "Porsche Old 911", 
        "Lexus": "Lexus ES 300h", 
        "Tesla": "Tesla Cybertruck", 
        "Mitsubishi": "Mitsubishi Lancer 2.0 GTE",
        "Chevrole": "Chevrole Corvette C5 Z06"
    }
    
    product = Product.query.filter_by(name=type_dict[carType]).first()
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
