import sys, src.database, src.deck, src.pdf

args = sys.argv

if '.txt' in args[-1]: src.deck.PATH = args[-1]
elif '.com' in args[-1]: src.deck.PATH = args[-1]; src.deck.isURL = True
else: src.deck.PATH = input('Enter Deck Path: ')

print(f"Loading deck at path: {src.deck.PATH}")

if '--update' in args or '-u' in args: src.database.Update()

if src.deck.isURL: myDeck = src.deck.Load({'name': args[-1].split('/')[-1]})
else: myDeck = src.deck.Load({'name': src.deck.PATH.replace('.txt','')})

pdf = src.pdf.Make(myDeck)

print('Proxy PDF Complate!')
