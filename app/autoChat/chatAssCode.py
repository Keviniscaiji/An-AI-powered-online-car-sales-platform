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
        "questions": ["你们的营业时间是什么时候？", "你们什么时候开门？", "你们什么时候关门？"],
        "intent": "business_hours",
        "answer": "我们的营业时间是周一至周五上午9点至下午5点。",
    },
    {
        "questions": ["怎么联系你们？", "你们的联系方式是什么？"],
        "intent": "contact_info",
        "answer": "您可以通过电话：123-456-7890，或者通过电子邮件：contact@example.com联系我们。",
    },
]

# 预处理问题
def preprocess_question(question):
    tokens = nltk.word_tokenize(question)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.lower() not in stopwords.words("chinese")]
    return tokens

# 计算问题之间的相似度
def question_similarity(q1, q2):
    q1_words = set(preprocess_question(q1))
    q2_words = set(preprocess_question(q2))
    return len(q1_words.intersection(q2_words)) / len(q1_words.union(q2_words))

# 获取回答
def get_answer(user_question):
    max_similarity = 0
    best_answer = "抱歉，我无法回答您的问题。"
    for item in data:
        for question in item["questions"]:
            similarity = question_similarity(user_question, question)
            if similarity > max_similarity:
                max_similarity = similarity
                best_answer = item["answer"]
    return best_answer

# 与机器人聊天
# while True:
#     user_input = input("用户：")
#     if user_input.lower() == "退出":
#         break
#     response = get_answer(user_input)
#     print("智能客服：", response)
