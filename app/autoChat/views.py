from flask import render_template, session, redirect, url_for, request, jsonify
from . import autoChat
from nltk.chat.util import Chat, reflections

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import random

# 下载必要的nltk数据包
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

lemmatizer = WordNetLemmatizer()

# 示例数据：问题、意图和回答
data = [
    {
        "questions": ["When are your business hours?", "When do you open?", "When do you close?"],
        "intent": "business_hours",
        "answer": "Our business hours are from 9 a.m. to 5 p.m., Monday through Friday.",
    },
    {
        "questions": ["How can I contact you?", "What is your contact information?"],
        "intent": "contact_info",
        "answer": "You can contact us by phone: 132-132-1321, or by email: autowheel@ucd.com.",
    },
    {
        "questions": ["What kind of website are you?", "What services does your website provide?"],
        "intent": "about_info",
        "answer": "We are an online car sales website. We hope to combine modern artificial intelligence methods with "
                  "traditional websites to provide better services for our customers.",
    },
    {
        "questions": [""],
        "intent": "contact_info",
        "answer": "You can contact us by phone: 132-132-1321, or by email: autowheel@ucd.com.",
    },
    {
        "questions": ["How can I create an account?", "What is the registration process?"],
        "intent": "account_creation",
        "answer": "To create an account, click on the 'Sign Up' button on our homepage, fill in the required information, and follow the instructions to complete the registration process.",
    },
    {
        "questions": ["How do I reset my password?", "I forgot my password, what should I do?"],
        "intent": "password_reset",
        "answer": "To reset your password, click on the 'Forgot Password' link on the login page, enter your email "
                  "address, and follow the instructions sent to your email to set a new password.",
    },
    {
        "questions": ["Can I return a purchased car?", "What is your return policy?"],
        "intent": "return_policy",
        "answer": "Yes, you can return a purchased car within 14 days of delivery, provided it meets our return "
                  "policy criteria. Please refer to our 'Return Policy' page on our website for more information.",
    },
    {
        "questions": ["What payment methods do you accept?", "How can I pay for my purchase?"],
        "intent": "payment_methods",
        "answer": "We accept various payment methods, including credit cards, debit cards, and bank transfers. You can choose the most convenient method for you during the checkout process.",
    },
]


# 预处理问题
def preprocess_question(question):
    tokens = nltk.word_tokenize(question)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if
              token.lower() not in stopwords.words("chinese")]
    return tokens


# 计算问题之间的相似度
def question_similarity(q1, q2):
    q1_words = set(preprocess_question(q1))
    q2_words = set(preprocess_question(q2))
    return len(q1_words.intersection(q2_words)) / len(q1_words.union(q2_words))


# 获取回答
def get_answer(user_question):
    max_similarity = 0
    best_answer = "Sorry I can not reply your question"
    for item in data:
        for question in item["questions"]:
            similarity = question_similarity(user_question, question)
            if similarity > max_similarity:
                max_similarity = similarity
                best_answer = item["answer"]
    return best_answer


@autoChat.route('/autoChat/index', methods=['POST', 'GET'])
def index():
    return render_template('autoChat/index.html')


# 加载聊天数据

# pairs = [
#     ['hi', ['Hello', 'Hi', 'Hey']],
#     ['bye', ['Goodbye', 'Bye', 'See you later']],
#     ['thank you', ['You are welcome', 'No problem']],
#     ['my name is (.*)', ['Hi %1, how can I help you?']],
#     ['default', ["I don't understand", 'Please ask another question']]
# ]
#
# # 创建 Chat 对象
# chatbot = Chat(pairs, reflections)


# 定义聊天接口
@autoChat.route('/chat', methods=['POST', 'GET'])
def chat():
    # 获取用户输入的文本
    user_text = request.form['message']
    # 使用 Chat 对象处理用户输入，返回聊天结果
    # response_text = str(chatbot.respond(user_text))
    response_text = get_answer(user_text)
    return jsonify({'text': response_text})

#
#
# @auth.route('/auth/register')
# def register():
#
#     return render_template('auth/register.html')
