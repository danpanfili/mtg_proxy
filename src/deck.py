import src.database as db
import requests

isURL = False

def Load(info={}):
    if isURL: deck_text = requests.get(PATH).text.replace('\r','').splitlines()
    else:
        with open(PATH, 'r') as file:
            deck_text = file.readlines()
    
    deck = {
        'info':info,
        'card':[]}
    
    for line in deck_text:
        if line == '\n' or line == '': continue

        line = line.split(' ')
        copies = int(line[0])
        name = ' '.join(line[1:]).replace('\n','').replace('/',' // ')
        for c in range(copies):
            key = [key for key in db.CARDS.keys() if name in key]
            deck['card'] += [db.CARDS[key[0]][0]]

    return deck
