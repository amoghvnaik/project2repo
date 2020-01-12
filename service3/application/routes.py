import random
from application import app

@app.route('/')
def random_letter():
    random_letter = chr(random.randrange(65, 68))
    return {"letter":random_letter}

