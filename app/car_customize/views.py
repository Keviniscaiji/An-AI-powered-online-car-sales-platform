from flask import render_template, session, redirect, url_for
from . import car_customize


@car_customize.route('/car_customize')
def index():
    return render_template('car_customize/index.html')

