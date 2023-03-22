from flask import render_template, session, redirect, url_for
from . import auth


@auth.route('/imgSearch/login')
def imgSearch():
    return render_template('imgSearch/imgSearch.html')
#
#
# @auth.route('/auth/register')
# def register():
#
#     return render_template('auth/register.html')
