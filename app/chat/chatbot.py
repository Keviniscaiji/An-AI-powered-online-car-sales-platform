import random
def get_response(message):
    responses = [
        "I'm sorry, I don't understand.",
        "Can you please rephrase that?",
        "I'm not sure what you mean.",
        "Could you provide more context?",
    ]
    return random.choice(responses)
