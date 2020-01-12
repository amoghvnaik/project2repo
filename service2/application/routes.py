from random import randint
from application import app

@app.route('/')
def random_number():
    random_number = str(randint(0, 2))
    return {"number":random_number}
