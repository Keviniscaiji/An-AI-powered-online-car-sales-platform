from flask import render_template, session, redirect, url_for
from . import car_customize


@car_customize.route('/car_customize')
def index():
    return render_template('car_customize/index.html')


from flask import request, jsonify


@car_customize.route('/car_customize', methods=['POST'])
def handle_colors():
    data = request.get_json()
    car_color = data.get('carColor')
    # light_color = data.get('lightColor')



    return jsonify({'status': 'success'})
