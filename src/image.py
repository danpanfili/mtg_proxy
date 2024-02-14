import urllib.request
import src.database as db
from io import BytesIO

def Load(name, img_type = 'png'):
    if 'card_faces' in db.CARDS[name][0].keys():
        if len(db.CARDS[name][0]['card_faces']) > 1 and 'image_uris' in db.CARDS[name][0]['card_faces'][0].keys(): url = [face['image_uris'][img_type] for face in db.CARDS[name][0]['card_faces']]
        else: url = [db.CARDS[name][0]['image_uris'][img_type]]
    else:
        url = [db.CARDS[name][0]['image_uris'][img_type]]

    image_data = []
    for u in url:
        with urllib.request.urlopen(u) as response:
            image_data += [BytesIO(response.read())]

    return image_data

def Load4Deck(deck, include_basics = False):
    print("Loading Deck Images...")

    images = []
    basics = ['Swamp', 'Mountain', 'Plains', 'Island', 'Forest']
    for card in deck['card']:
        if include_basics: 
            images += Load(card['name'], 'large')
        elif card['name'] not in basics:
            images += Load(card['name'], 'large')
    return images