import requests
from application import app

@app.route('/')
def proverb():
    random_number = requests.get('http://service2:5001').json()["number"]
    random_letter = requests.get('http://service3:5002').json()["letter"]
    if random_number=='0' and random_letter=='A':
        return {"proverb":"Number: 0, Letter: A, Proverb: A bird in hand is worth two in the bush"}
    elif random_number=='0' and random_letter=='B':
        return {"proverb":"Number: 0, Letter: B, Proverb: Beauty is in the eye of the beholder"}
    elif random_number=='0' and random_letter=='C':
        return {"proverb":"Number: 0, Letter: C, Proverb: Better late than never"}
    elif random_number=='1' and random_letter=='A':
        return {"proverb":"Number: 1, Letter: A, Proverb: Rome wasn't built in a day"}
    elif random_number=='1' and random_letter=='B':
        return {"proverb":"Number: 1, Letter: B, Proverb: Actions speak louder than words"}
    elif random_number=='1' and random_letter=='C':
        return {"proverb":"Number: 1, Letter: C, Proverb: Never judge a book by its cover"}
    elif random_number=='2' and random_letter=='A':
        return {"proverb":"Number: 2, Letter: A, Proverb: Strike while the iron is hot"}
    elif random_number=='2' and random_letter=='B':
        return {"proverb":"Number: 2, Letter: B, Proverb: The early bird catches the worm"}
    elif random_number=='2' and random_letter=='C':
        return {"proverb":"Number: 2, Letter: C, Proverb: Better safe than sorry"}
    elif random_number=='3' and random_letter=='A':
        return {"proverb":"Number: 3, Letter: A, Proverb: A bad workman always blames his tools"}
    elif random_number=='3' and random_letter=='B':
        return {"proverb":"Number: 3, Letter: B, Proverb: Absence makes the heart grow fonder"}
    elif random_number=='3' and random_letter=='C':
        return {"proverb":"Number: 3, Letter: C, Proverb: A chain is only as strong as its weakest link"}
    elif random_number=='4' and random_letter=='A':
        return {"proverb":"Number: 4, Letter: A, Proverb: A journey of a thousand miles begins with a single step"}
    elif random_number=='4' and random_letter=='B':
        return {"proverb":"Number: 4, Letter: B, Proverb: Every cloud has a silver lining"}
    elif random_number=='4' and random_letter=='C':
        return {"proverb":"Number: 4, Letter: C, Proverb: Good things come to those who wait"}
    elif random_number=='5' and random_letter=='A':
        return {"proverb":"Number: 5, Letter: A, Proverb: Practice makes perfect"}
    elif random_number=='5' and random_letter=='B':
        return {"proverb":"Number: 5, Letter: B, Proverb: There is no time like the present"}
    elif random_number=='5' and random_letter=='C':
        return {"proverb":"Number: 5, Letter: C, Proverb: Where one door shuts, another opens"}
