from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
# from .forms import NameForm
from .. import db
from ..models import User


@main.route('/')
def index():  # put application's code here
    return render_template('index.html')


@main.route('/about')
def about():  # put application's code here
    return render_template('about.html')


@main.route('/cars')
def cars():
    return render_template('car.html')


@main.route('/car-single')
def car_single():
    return render_template('car-single.html')


@main.route('/blog')
def blog():
    return render_template('blog.html')


@main.route('/blog-single')
def blog_single():
    return render_template('blog-single.html')


@main.route('/pricing')
def pricing():
    return render_template('pricing.html')


@main.route('/services')
def services():
    return render_template('services.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/imageSearch')
def imageSearch():
    return render_template('imageSearch.html')