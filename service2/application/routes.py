from random import randint
from application import app

@app.route('/', methods=['POST'])
def random_number():
    random_number = str(randint(3, 5))
    return {"number":random_number}
