from flask import Blueprint

autoChat = Blueprint('autoChat', __name__)

from . import views


# 与机器人聊天
# while True:
#     user_input = input("用户：")
#     if user_input.lower() == "退出":
#         break
#     response = get_answer(user_input)
#     print("智能客服：", response)
