from flask import render_template, request, jsonify
from flask_socketio import emit, join_room, leave_room, \
    close_room
import random
import datetime
from sqlalchemy import and_, or_
import os

from . import chat
from app import socketio, db
from app.models import Message, Product
from config import basedir

from .fasttext_backend import prepare_models, predict_text, predict_text_all


models = prepare_models()


# View Functions
@chat.route('/', methods=['POST', 'GET'])
def index():
    return render_template('customer_chat.html')


@chat.route('/bot', methods=['POST'])
def bot():
    if request.method == 'POST':
        text = request.values['msg-to-bot']
        preds = predict_text_all(text, models, 50)
        brand = preds['brands']
        product = preds['products']
        intent = preds['intents']
        prod = Product.query.filter_by(name=product).first()
        response = dict()
        if intent == "AUTOMATIC-PILOT":
            for category in prod.categories:
                if category.name == "Autonomous":
                    is_auto = True
                else:
                    is_auto = False
            response['msg-back'] = "Autonomous Driving System (ADS) {} supported on {}.".format(
                "is" if is_auto else "is not", prod.name
            )
        elif intent == "PRICE":
            response['msg-back'] = "The overall estimated price of {} is ${}".format(
                prod.name, prod.price
            )
        elif intent == "PERFORMANCE":
            response['msg-back'] = "The maximum speed of {} is {}, while its oil consumption per mile is {} liters.".format(
                prod.name, prod.max_speed, prod.oil_consumption
            )
        else:
            response['msg-back'] = "We currently have five independent cars that support customization: "
            for item in [
                'tesla truck',
                'infiniti',
                'chevrole zr1',
                'lexus lc500h',
                'Porsche 911',
                'Porsche old 911']:
                response['msg-back'] += item + ", "
            response['msg-back'] += "<br><br> Please access {} to customize your own color.".format(
                "http://ipa-009.ucd.ie/car_customize"
            )
        return jsonify(response)
    


@chat.route('/admin', methods=['POST', 'GET'])
def admin_chat():
    # print("okk")
    return render_template('admin/app-chat-box.html')


# Basic Operations
@socketio.on('join', namespace='/chatroom')
def join(message):
    leave_room("waiting")
    join_room(message['room'])
    emit('join_response', message, room=message['room'])


@socketio.on('leave', namespace='/chatroom')
def leave(message):
    leave_room(message['room'])
    emit('leave_response', message, room=message['room'])


@socketio.on('close', namespace='/chatroom')
def close(message):
    if message['room'] != 'waiting':
        close_room(message['room'])


@socketio.on('customer_reconnect', namespace='/chatroom')
def customer_reconnect(message):
    leave_room(message['room'])
    join_room("waiting")
    emit('leave_response', message, room=message['room'])
    emit('user_wait_response', {'room_name': "waiting", "user": message["user"]}, room='waiting')


@socketio.on('send', namespace='/chatroom')
def send(message):
    msg = Message(
        user_from=message['user'],
        user_to="admin" if message['user'] != "admin" else message['room'][13:],
        msg=message['msg'],
        type=0,
        time=datetime.datetime.now()
    )
    db.session.add(msg)
    db.session.commit()
    emit('msg_response', message, room=message['room'])


@socketio.on('send_img', namespace='/chatroom')
def send_img(message):
    # print("okk0")
    filename = message['file_name']
    current_time = datetime.datetime.now().strftime('%H%M%S%Y%m%d')
    rand_seed = random.randint(1, 9999)
    strong_filename = "{}_{}_{}".format(current_time, rand_seed, filename)
    f = open(os.path.join(basedir, 'app', 'static', 'storage', 'cache', strong_filename), 'wb')
    f.write(message['img'])
    f.close()
    msg = Message(
        user_from=message['user'],
        user_to="admin" if message['user'] != "admin" else message['room'][13:],
        msg="../../static/storage/cache/{}".format(strong_filename),
        type=1,
        time=datetime.datetime.now()
    )
    db.session.add(msg)
    db.session.commit()
    emit('img_response', message, room=message['room'])
    # print("okk1")


# Administrators Operations
@socketio.on('admin_join_wait', namespace='/chatroom')
def admin_join_wait(message):
    join_room('waiting')
    print("OK")
    emit('admin_join_wait_response', {'room_name': message['room']}, room='waiting')


@socketio.on('admin_accept', namespace='/chatroom')
def admin_accept(message):
    join_room("chat_channel_" + message['user'])
    emit('admin_accept_response', {'room_name': 'waiting', 'user': message['user']}, room='waiting')


@socketio.on('admin_request_recover', namespace='/chatroom')
def admin_request_recover(message):
    username = message['user']
    msg_history = Message.query.filter(
        or_(
            and_(Message.user_from == username, Message.user_to == "admin"),
            and_(Message.user_from == "admin", Message.user_to == username)
        )).order_by(Message.time).all()
    msg_recovers = {"length": len(msg_history)}
    for i, msg_recover in enumerate(msg_history):
        _msg = msg_recover.msg
        _time = str(msg_recover.time)
        _time = _time[11:16] + ", " + _time[0:10]
        msg_recovers[str(i)] = {
            "msg": _msg,
            "time": _time,
            "user": msg_recover.user_from,
            "type": msg_recover.type}
    emit('msg_recover_response', msg_recovers, room=message['room'])


# Customer Operations
@socketio.on('user_join_wait', namespace='/chatroom')
def user_join_wait(message):
    join_room('waiting')
    emit('user_wait_response', {'room_name': "waiting", "user": message["user"]}, room='waiting')
