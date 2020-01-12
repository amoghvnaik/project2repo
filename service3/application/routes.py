import random
from application import app

@app.route('/', methods=['GET'])
def random_letter():
    random_letter = chr(random.randrange(65, 68))
    return {"letter":random_letter}

