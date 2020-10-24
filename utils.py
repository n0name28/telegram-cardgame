import os.path
from os import listdir
from os.path import isfile, join
import random

import sys
from PIL import Image

def combine_images(cards,name):
    images = []
    for image in cards:
        images.append(Image.open('images/%s' % image))
    new_im = Image.new('RGB', (210, 107))
    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += 70
    new_im.save(name)



def get_score(cards):
    score = 0
    for card in cards:
        num = int(card.split('-')[0])
        score += num
    return score

def get_random_cards():
    path = 'images'
    out = []
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for i in range(1,4):
        rand = random.randint(0,len(onlyfiles)-1)
        out.append(onlyfiles[rand])
        onlyfiles.pop(rand)
    return out

def get_data():
    if not os.path.isfile('secret'):
        bot_name = input('Имя бота:')
        secret = input('Cекретный ключ:')
        f = open('secret','w')
        mystr = '%s:%s' % (bot_name,secret)
        f.write(mystr)
        f.close()
    else:
        f = open('secret','r')
        mystr = f.read()
        arr = mystr.split(';')
        bot_name = arr[0]
        key = arr[1]
    
    data = {
        'name': bot_name,
        'key': key
    }
    return data



def get_computer_cards(computer_cards):
    if len(computer_cards) == 0:
        computer_cards = get_random_cards()
        combine_images(computer_cards,'comp_cards.png')
    return computer_cards


def refresh_game():
    computer_cards = []

def get_rezult(computer_cards,player_cards):
    print(computer_cards)
    print(player_cards)
    print(get_score(computer_cards))
    print(get_score(player_cards))
    if get_score(computer_cards) > get_score(player_cards):
        return 'Компьютер выйграл с %s' % get_score(computer_cards)
    if get_score(computer_cards) > get_score(player_cards):
        return 'Вы выйграли, у комьютера %s' % get_score(computer_cards)
    if get_score(computer_cards) == get_score(player_cards):
        return 'Ничья'
