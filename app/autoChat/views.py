import json

from flask import render_template, session, redirect, url_for, request, jsonify
from . import autoChat
from nltk.chat.util import Chat, reflections

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import random


# nltk.download("stopwords")

lemmatizer = WordNetLemmatizer()



data = [
    {
        "questions": ["Hello!", "Hi!", "Hey!", "Greetings!"],
        "intent": "greeting",
        "answer": "Hello! How can I help you today?"
    },
    {
        "questions": ["Good morning!", "Morning!", "Hi, good morning!"],
        "intent": "morning_greeting",
        "answer": "Good morning! What can I do for you?"
    },
    {
        "questions": ["Good afternoon!", "Afternoon!", "Hi, good afternoon!"],
        "intent": "afternoon_greeting",
        "answer": "Good afternoon! How may I assist you?"
    },
    {
        "questions": ["Good evening!", "Evening!", "Hi, good evening!"],
        "intent": "evening_greeting",
        "answer": "Good evening! What can I help you with?"
    },
    {
        "questions": ["Good night!", "Night!", "Bye, good night!"],
        "intent": "night_greeting",
        "answer": "Good night! If you have any more questions, feel free to ask anytime."
    },
    {
        "questions": ["When are your business hours?", "When do you open?", "When do you close?"],
        "intent": "business_hours",
        "answer": "Our business hours are from 9 a.m. to 5 p.m., Monday through Friday."
    },
    {
        "questions": ["How can I contact you?", "What is your contact information?"],
        "intent": "contact_info",
        "answer": "You can contact us by phone: 132-132-1321, or by email: autowheel@ucd.com."
    },
    {
        "questions": ["What kind of website are you?", "What services does your website provide?"],
        "intent": "about_info",
        "answer": "We are an online car sales website. We hope to combine modern artificial intelligence methods with traditional websites to provide better services for our customers."
    },
    {
        "questions": ["How can I contact you"],
        "intent": "contact_info",
        "answer": "You can contact us by phone: 132-132-1321, or by email: autowheel@ucd.com."
    },
    {
        "questions": ["How can I create an account?", "What is the registration process?"],
        "intent": "account_creation",
        "answer": "To create an account, click on the 'Sign Up' button on our homepage, fill in the required information, and follow the instructions to complete the registration process."
    },
    {
        "questions": ["How do I reset my password?", "I forgot my password, what should I do?"],
        "intent": "password_reset",
        "answer": "To reset your password, click on the 'Forgot Password' link on the login page, enter your email address, and follow the instructions sent to your email to set a new password."
    },
    {
        "questions": ["Can I return a purchased car?", "What is your return policy?"],
        "intent": "return_policy",
        "answer": "Yes, you can return a purchased car within 14 days of delivery, provided it meets our return policy criteria. Please refer to our 'Return Policy' page on our website for more information."
    },
    {
        "questions": ["What payment methods do you accept?", "How can I pay for my purchase?"],
        "intent": "payment_methods",
        "answer": "We accept various payment methods, including credit cards, debit cards, and bank transfers. You can choose the most convenient method for you during the checkout process."
    }
]


# Preprocess questions

def preprocess_question(question):
    tokens = nltk.word_tokenize(question)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if
              token.lower() not in stopwords.words("english")]
    return tokens


# Calculate similarity between questions
def question_similarity(q1, q2):
    q1_words = set(preprocess_question(q1))
    q2_words = set(preprocess_question(q2))
    return len(q1_words.intersection(q2_words)) / len(q1_words.union(q2_words))


# Get answer
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




# Define chat interface
@autoChat.route('/chat', methods=['POST', 'GET'])
def chat():
    # Get the text input from the user
    user_text = request.form['message']
    # Use Chat object to handle user input and return chat result
    # response_text = str(chatbot.respond(user_text))
    response_text = get_answer(user_text)
    return jsonify({'text': response_text})
