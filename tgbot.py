import random

import telebot

bot = telebot.TeleBot("6060190526:AAHqT7w0aBVIvlmPE_MfrUbbZ0jnmL2xgbE")

sweets = 55
max_sweets = 28
user_turn = 0
bot_turn = 0
flag = ""


@bot.message_handler(commands = ["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id,f"Приветсвую вас в игре!")
    flag = random.choice(["user","bot"])
    if flag == "user":
        bot.send_message(message.chat.id,f"Первым ходите вы")
        controller(message)
    else:
        bot.send_message(message.chat.id,f"Первым ходит бот")
        controller(message)

def controller(message):
    global flag
    if sweets >0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Ваш ход. Введите кол-во конфет от 0 до {max_sweets}")
            bot.register_next_step_handler(message,user_input)
        else:
            bot_input(message)

    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}")

def bot_input(message):
    global sweets,bot_turn, flag
    if sweets <=max_sweets:
        bot_turn = sweets
    elif sweets % max_sweets == 0:
        bot_turn = max_sweets - 1
    else:
        bot_turn = sweets % max_sweets -1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"бот взял {bot_turn} конфеты")
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

def user_input(message):
    global flag,sweets, user_turn
    user_turn = int(message.text)
    sweets -= user_turn
    flag = "user" if flag == "bot" else "bot"
    bot.send_message(message.chat.id, f"осталось {sweets}")
    controller(message)

bot.infinity_polling()