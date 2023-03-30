from flask import render_template, session, redirect, url_for
from . import carCostumize


@carCostumize.route('/carCostumize')
def carCostumize():
    return render_template('carCostumize/carCostumize.html')

