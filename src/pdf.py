import src.image as img_tool
import numpy as np
from PIL import Image

info = {
    'paper':{
        'letter': {'size': np.array([8.5, 11])},
        'a4': {'size': np.array([8.3, 11.7])}
    },   
    'card':{
        'mtg': {'size': np.array([2.48, 3.48])},
        'mtg_large': {'size': np.array([3.5, 5])},
    }
}

def Make(deck, include_basics = False, cards_per_page = 3, params = {'paper_type':'a4', 'card_type':'mtg'}):
    print('Making PDF...')

    images = img_tool.Load4Deck(deck, include_basics)

    paper_size =   info['paper'][params['paper_type']]['size']
    card_size =     info['card'][params['card_type']]['size']
    margin_size =   paper_size - (card_size*3)

    template_size = np.array(Image.open(images[0]).size)*3

    dpi = template_size / card_size / cards_per_page
    margin_start = (dpi * (margin_size/2)).astype(np.uint32)
    
    template = Image.new('RGB', (template_size + margin_start*2).tolist(), color = 'white')

    pdf = []

    for i,image in enumerate(images):
        if (i%9 == 0 and i > 0) or i == len(images): 
            pdf += [template]
            template = Image.new('RGB', (template_size + margin_start*2).tolist(), color = 'white')

        row = i // cards_per_page % cards_per_page
        col = i % cards_per_page


        with Image.open(image) as img:
            start_pos = np.array([col * img.size[0], row * img.size[1]]) + margin_start
            template.paste(img, tuple(start_pos))

    pdf_name = 'deck.pdf'
    if 'name' in deck['info'].keys(): pdf_name = pdf_name.replace('deck', deck['info']['name'])

    pdf[0].save(pdf_name,'PDF',save_all=True,append_images=pdf[1:], dpi=tuple(pdf[0].size/card_size/3))

    return pdf