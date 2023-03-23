from flask import render_template, session, redirect, url_for
from . import chat


@chat.route('/chat/login')
def chat():
    return render_template('chat/imgSearch.html')
#
#
# @auth.route('/auth/register')
# def register():
#
#     return render_template('auth/register.html')
