from flask import render_template, session, redirect, url_for
from . import chat


@chat.route('/chat/admin_chat')
def admin_chat():
    return render_template('chat/admin_chat.html')

@chat.route('/chat/customer_chat')
def customer_chat():
    return render_template('chat/customer_chat.html')
#
#
# @auth.route('/auth/register')
# def register():
#
#     return render_template('auth/register.html')
