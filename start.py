from utils import get_data, get_random_cards, get_score, combine_images, get_computer_cards, get_rezult

data = get_data()
name = data['name']
key = data['key']
print('Start bot %s' % name)

import telebot


bot = telebot.TeleBot(key)

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
markup = InlineKeyboardMarkup()
markup.add(InlineKeyboardButton('Вскрыться',callback_data='one'))
markup.add(InlineKeyboardButton('Дать дальше',callback_data='two'))
markup.add(InlineKeyboardButton('Упасть',callback_data='tree'))


computer_cards = []
player_cards = []
TEST = 'hello'


@bot.callback_query_handler(lambda first: first.data=="one")
def button_send(query):
    #bot.send_message(query.message.chat.id, 'Вы вскрылись!')
    print(TEST)
    comp_cards = get_computer_cards(computer_cards)
    bot.send_photo(chat_id=query.message.chat.id, photo=open('comp_cards.png', 'rb'))
    bot.send_message(query.message.chat.id, get_rezult(comp_cards,player_cards))

@bot.callback_query_handler(lambda first: first.data=="two")
def button_send(query):
    bot.send_message(query.message.chat.id, 'Вы дали дальше!')
    comp_cards = get_computer_cards(computer_cards)

@bot.callback_query_handler(lambda first: first.data=="tree")
def button_send(query):
    #bot.send_message(query.message.chat.id, 'Вы упали!')
    computer_cards = get_computer_cards(computer_cards)
    bot.send_photo(chat_id=query.message.chat.id, photo=open('comp_cards.png', 'rb'))
    bot.send_message(query.message.chat.id, get_rezult(computer_cards,player_cards))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    room_id = message.chat.id
    #bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    #bot.send_photo(chat_id=room_id, photo=open('images/resized-2C.png', 'rb'))
    player_cards = get_random_cards()
    score = get_score(player_cards)
    bot.send_message(message.chat.id, 'Вы набрали: %s!' % score, reply_markup=markup)
    combine_images(player_cards,'player.png')
    bot.send_photo(chat_id=room_id, photo=open('player.png', 'rb'))
    TEST = 'ffffff'
    print(TEST)

bot.polling()

#sprint(get_random_cards())