from flask import render_template, session, redirect, url_for, request, jsonify
from . import autoChat
from nltk.chat.util import Chat, reflections


@autoChat.route('/autoChat/index', methods=['POST', 'GET'])
def index():
    return render_template('autoChat/index.html')


# 加载聊天数据

pairs = [
    ['hi', ['Hello', 'Hi', 'Hey']],
    ['bye', ['Goodbye', 'Bye', 'See you later']],
    ['thank you', ['You are welcome', 'No problem']],
    ['my name is (.*)', ['Hi %1, how can I help you?']],
    ['default', ["I don't understand", 'Please ask another question']]
]

# 创建 Chat 对象
chatbot = Chat(pairs, reflections)


# 定义聊天接口
@autoChat.route('/chat', methods=['POST', 'GET'])
def chat():
    # 获取用户输入的文本
    user_text = request.form['message']
    # 使用 Chat 对象处理用户输入，返回聊天结果
    response_text = str(chatbot.respond(user_text))
    # return the reply
    # return "response_text"
    return jsonify({'text': "?"})

#
#
# @auth.route('/auth/register')
# def register():
#
#     return render_template('auth/register.html')
