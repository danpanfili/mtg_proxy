import pickle, requests, os

def Download(bulk_url = r'https://api.scryfall.com/bulk-data/default-cards/'):
    print("Downloading most recent database...")
    response = requests.get(bulk_url).json()
    download_url = response['download_uri']
    
    return requests.get(download_url).json()

def Update(filename = 'src/cards.pkl'):
    print("Updating local database...")

    database = Download()

    cards = {}
    for entry in database:
        if entry['layout'] == 'art_series':
            1
        elif entry['name'] not in cards.keys():
            cards[entry['name']] = [entry]
        else:
            cards[entry['name']] += [entry]

    with open(filename, '+wb') as file:
        pickle.dump(cards, file)

    return cards

def Load(filename = 'src/cards.pkl'):
    print("Loading Database...")
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    else:
        return Download(filename)
    
CARDS = Load()
