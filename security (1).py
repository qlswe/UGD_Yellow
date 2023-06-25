import telebot
import random
import time
from telebot import types
import requests
import json
import datetime
import logging


bot = telebot.TeleBot('TOKEN')
API = 'TOKEN OPENWEATHER'


# =====================================================
captcha_list = ["яблоко", "арбуз", "банан", "виноград", "морковь", "кукуруза"] # это название всех элементов с капчи, можете поставить что угодно
# ================
cp1 = "яблоко"  # смайлики в капче.
cp2 = "арбуз"
cp3 = "банан"
cp4 = "виноград"
cp5 = "морковь"
cp6 = "кукуруза"
# ================
completecaptcga = [ID YOUR BOT OR YOURS]
# вместо ID YOUR BOT OR YOURS вставьте ID, у которого никогда не будет требовать капчу!


@bot.message_handler(content_types=["new_chat_members"])
def scanning(message):
    name = message.new_chat_members[0].first_name
    bot.send_message(message.chat.id, f"Добро пожаловать, {name}! \nВот наши правила:\n✅-можно❌-нельзя \nоскорблять людей❌\nотправлять ссылки на другие группы-✅\nматериться-❌\nотправлять 18+-❌\nспамить-❌\nдобавлять людей-✅")
    ms = message.chat.id
    if ms in completecaptcga:
        bot.send_message(message.chat.id, ' Вы уже прошли проверку') # если юзер прошел проверку, тут уже вашего бота вставлять
    else:
        # Это внутреняя клавиатура, которая содержит в себе символы, на которые нажимает человек.
        keyboard = types.InlineKeyboardMarkup()
        cpt1 = types.InlineKeyboardButton(text=cp1, callback_data="cpt1")
        cpt2 = types.InlineKeyboardButton(text=cp2, callback_data="cpt2")
        cpt3 = types.InlineKeyboardButton(text=cp3, callback_data="cpt3")
        keyboard.add(cpt1, cpt2, cpt3)
        cpt1 = types.InlineKeyboardButton(text=cp4, callback_data="cpt4")
        cpt2 = types.InlineKeyboardButton(text=cp5, callback_data="cpt5")
        cpt3 = types.InlineKeyboardButton(text=cp6, callback_data="cpt6")
        keyboard.add(cpt1, cpt2, cpt3)
        markdown = """
        *bold text*
        _italic text_
        [text](URL)
        """
        global emoji
        emoji = random.choice(captcha_list)
        global dostup
        dostup = 0
        # само сообщение с капчей.
        bot.send_message(message.chat.id, ' Чтобы продолжить пользоваться ботом, выберите на клавиатуре ' + '*' + emoji + '*', parse_mode="Markdown", reply_markup=keyboard)


# тут проверки, верно ли нажал человек. Изменять только текст, остальное не трогать!
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "cpt1":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу на сегодня!')
            else:
                check = captcha_list[0:1]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ у вас осталась одна попытка напишите /scan что бы повторить попытку.')
        if call.data == "cpt2":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[1:2]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')
        if call.data == "cpt3":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[2:3]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')
        if call.data == "cpt4":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[3:4]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')
        if call.data == "cpt5":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[4:5]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')
        if call.data == "cpt6":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[5:6]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')


captcha_list = ["телефон", "ноутбук", "планшет", "датчик", "телевизор", "микроволновка"] # это название всех элементов с капчи, можете поставить что угодно
# ================
cp1 = "телефон"  # смайлики в капче.
cp2 = "ноутбук"
cp3 = "планшет"
cp4 = "датчик"
cp5 = "телевизор"
cp6 = "микроволновка"


completecaptcga = [6084496194]
# вместо 999 вставьте ID, у которого никогда не будет требовать капчу!


@bot.message_handler(commands=['scan'])
def scanning2(message):
    ms = message.chat.id
    if ms in completecaptcga:
        bot.send_message(message.chat.id, ' Вы уже прошли проверку') # если юзер прошел проверку, тут уже вашего бота вставлять
    else:
        # Это внутреняя клавиатура, которая содержит в себе символы, на которые нажимает человек.
        keyboard = types.InlineKeyboardMarkup()
        cpt1 = types.InlineKeyboardButton(text=cp1, callback_data="cpt1")
        cpt2 = types.InlineKeyboardButton(text=cp2, callback_data="cpt2")
        cpt3 = types.InlineKeyboardButton(text=cp3, callback_data="cpt3")
        keyboard.add(cpt1, cpt2, cpt3)
        cpt1 = types.InlineKeyboardButton(text=cp4, callback_data="cpt4")
        cpt2 = types.InlineKeyboardButton(text=cp5, callback_data="cpt5")
        cpt3 = types.InlineKeyboardButton(text=cp6, callback_data="cpt6")
        keyboard.add(cpt1, cpt2, cpt3)
        markdown = """
        *bold text*
        _italic text_
        [text](URL)
        """
        global emoji
        emoji = random.choice(captcha_list)
        global dostup
        dostup = 0
        # само сообщение с капчей.
        bot.send_message(message.chat.id, ' Чтобы продолжить пользоваться ботом, выберите на клавиатуре ' + '*' + emoji + '*', parse_mode="Markdown", reply_markup=keyboard)


# тут проверки, верно ли нажал человек. Изменять только текст, остальное не трогать!
@bot.callback_query_handler(func=lambda call: True)
def reset(call):
    if call.message:
        if call.data == "cpt1":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу на сегодня!')
            else:
                check = captcha_list[0:1]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ у вас осталась одна попытка напишите /scanning что бы повторить попытку.')
        if call.data == "cpt2":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[1:2]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scann что бы повторить попытку')
        if call.data == "cpt3":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[2:3]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')
        if call.data == "cpt4":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[3:4]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')
        if call.data == "cpt5":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[4:5]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')
        if call.data == "cpt6":
            ms = call.message.chat.id
            if ms in completecaptcga:
                 bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
            else:
                check = captcha_list[5:6]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка выполнена')
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Не тот символ.У вас осталась одна попытка напишите /scan что бы повторить попытку')


#@bot.message_handler(func=lambda message: True, content_types=['sticker'])
#def handle_sticker(msg):
    #bot.delete_message(msg.chat.id, msg.message_id)
    #bot.send_message(msg.chat.id, "⚠️️все стикеры блокируются кодом")
    #По умолчанию сетод закоментирован но вы можете его включить в любой момент

@bot.message_handler(commands=['msgfrombot'])
def msg_from_bot(message):
    send = bot.send_message(message.chat.id, 'Введите id пользователя')
    bot.register_next_step_handler(send, msg_from_bot)


def msg_from_bot_1(message):
    global user_id
    user_id = message.text
    send = bot.send_message(message.chat.id, 'Введите сообщение')
    bot.register_next_step_handler(send, msg_from_bot_2)


def msg_from_bot_2(message):
    bot.send_message(user_id, '{}'.format(message.text))


@bot.message_handler(func=lambda message: message.text.lower() == "расстрелять")
def nas(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🔫|{tag1} тебя расстрелял(-а) {tag2}', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "покормить")
def eda(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🥄|{tag2} тебя покрмил(-а) с ложочки {tag1} ', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "поцеловать")
def poc(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'👩‍❤️‍💋‍👨|{tag1} тебя поцеловал(-а) {tag2} ', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "попрощаться")
def pok(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'👋|{tag1} попрощался с {tag2}', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "погладить")
def pogl(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'👋|{tag1}погладил(-а) {tag2} ', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "похоронить")
def pohoron(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f' 🪦|{tag1}похоронил(-a){tag2}) ', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "попить чай")
def chai(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🍵|{tag1} попил(-а) чай с {tag2}', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "ударить")
def udar(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'👊|{tag1} ударил(-а) {tag2} ', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "убить")
def udit(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'☠️|{tag1} убил(-а) {tag2} ', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "отсосать")
def command_text_dela(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'️|{tag1} отсосал(-а) у {tag2} ', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "утопить")
def command_text_del(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🚰️|{tag1} жестоко утопил(-а) {tag2} ', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "поприветствовать")
def command_text_priv(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'|{tag1} поприветствовал {tag2}', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "обнять")
def sos(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🤗|{tag1} обнял(-а) {tag2} ',  parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "запереть")
def sosi(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🔐|{tag1} закрыл(-а) в клетке {tag2}',  parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "сжечь")
def sosino(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🔥|{tag1} сжёг {tag2}',  parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "понюхать")
def sosik(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'👃🏻|{tag1} понухал(-а) {tag2}',  parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "ущипнуть")
def sosir(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🤏🏻|{tag1} ущипнул(-а){tag2}',  parse_mode='markdown')
    

@bot.message_handler(func=lambda message: message.text.lower() == "рп команды")
def rpcom(message):
    bot.send_message(message.chat.id, "Список доступных РП команд: \n1)Поприветствовать\n2)запереть\n3)обнять\n4)попращаться\n5)попить чай\n6)утопить\n7)убить\n8)расстрелять\n9)отсосать\n10)поприветствовать\n11)утопить\n12)погладить\n13)покормить\n14)похоронить\n15)поцеловать")

# обработчик команды /stats
@bot.message_handler(commands=['stats'])
def send_stats(message):
    bot_info = bot.get_me()
    subscribers = bot.get_chat_members_count(message.chat.id)
    text = f'Bot Name: {bot_info.first_name}\nUsername: @{bot_info.username}\nSubscribers:{subscribers}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['version'])
def version(message):
   bot.reply_to(message, 'python version: 3.10 Version bot:2.1 changes:[#b1e6974](https://github.com/qlswe/UGD_Yellow2.0/commit/eeaffaffdc6704f5cccc0b3c854433d490164030)', parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом. Напиши /help, чтобы начать использование и узнать, что я умею.")
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Your Text", url="Your link")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Your text", reply_markup=keyboard)


@bot.message_handler(commands=['YaGPT'])
def YaGPT(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="YaGPT", url="https://yandex.ru/project/alice/yagpt/index?utm_source=yadirect&utm_campaign=pp_ru_desktop_yandex_search_gpt&utm_term=виртуальный%20помощник%20алиса&utm_content=gpt&etext=2202.vdhTKFpiV1ar993rbEONJcRWe8hv_tVS8r6Qa-jkH6i_jpswvMlnTBFYKd7XTjTM4ACNAJflb4bsP09zgqf2XHdvbGhnampzbnBqZmxneWw.75bcd41cc5b0a53e8ca334cf67c40f7d886fc16a&yclid=2702180996062714309")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Опробовать YaGPT", reply_markup=keyboard)


@bot.message_handler(commands=['Your_command'])
def yandex(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Your text", url="Your link")
    keyboard.add(url_button)
    bot.send_photo(message.chat.id, "Your image")
    bot.send_message(message.chat.id, "Your link", reply_markup=keyboard)

# Функция для получения информации о загрузке CPU и RAM
def system_status():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024.0 ** 3), 2)
    available_memory = round(memory.available / (1024.0 ** 3), 2)
    used_memory = round(memory.used / (1024.0 ** 3), 2)
    memory_percent = memory.percent

    return f"CPU: {cpu_percent}%\n" \
           f"RAM: {used_memory} GB / {total_memory} GB ({memory_percent}%)\n" \
           f"Available RAM: {available_memory} GB"


# Обработка команды /status
@bot.message_handler(commands=['status'])
def send_status(message):
    sys_status = system_status()
    bot.reply_to(message, f"Текущее состояние системы:\n{sys_status}")


# Функция для получения списка пользователей в системе Windows
def get_users():
    users = []
    for user in psutil.users():
        if user.name not in users:
            users.append(user.name)
    return users


# Обработка команды /users
@bot.message_handler(commands=['users'])
def send_users(message):
    users = get_users()
    if users:
        reply_text = "Пользователи, которые в данный момент работают в системе:\n"
        for user in users:
            reply_text += f"{user}\n"
        bot.reply_to(message, reply_text)
    else:
        bot.reply_to(message, "В данный момент никто не работает в системе.")

@bot.message_handler(commands=['off'])
def off(message):
    bot.reply_to(message, "Выключение...")
    bot.reply_to(message, "Если захотите снова включить сделайте это через консоль сервра.")
    bot.reply_to(message, "Готово☑️")
    exit()


@bot.message_handler(commands=['rules'])
def rules(message):
    bot.reply_to(message, "Напиши /P1 что бы узнать правила бота.")


@bot.message_handler(commands=['P1'])
def P1(message):
    bot.reply_to(message, "\nПункт правил номер 1:🥳👋Первое и самое главное правило быть дружными и не спорить друг с другом особенно с администраторами чата.Следующий пункт правил /P2\n")


@bot.message_handler(commands=['P2'])
def P2(message):
    bot.reply_to(message, "\nПункт правил номер 2:⚠️⛔️Не флудить, спамить.Следующий пункт правил /P3\n")


@bot.message_handler(commands=['P3'])
def P3(message):
    bot.reply_to(message, "Пункт правил номер 3:🤬не матерится.(все маты будут удалены ботом)Cледующий пункт правил /P4.\n")


@bot.message_handler(commands=['P4'])
def P4(message):
    bot.reply_to(message, "\nПункт правил 4:📴Не выключать и не ломать ботаCледующий пункт правил /P5.\n")


@bot.message_handler(commands=['P5'])
def P5(message):
    bot.reply_to(message, "\nПункт правил номер 5:😜Говорить только на своем языке.Разрешенные языки:русский язык/английский/французский/беларусский.Cледующий пункт правил /P6.\n")


@bot.message_handler(commands=['P6'])
def P6(message):
    bot.reply_to(message, "\nПункт правил 6:🚫Не рекламировать ничего без согласия администратора(запрещены все виды рекламы).Cледующий пункт правил /P7.\n")


@bot.message_handler(commands=['P7'])
def P7(message):
    bot.reply_to(message, "\nПункт правил 7:💭Развод на деньги и т.д СТРОГО ЗАПРЕЩЕН.Cледующий пункт правил  /P8.\n")


@bot.message_handler(commands=['P8'])
def P8(message):
    bot.reply_to(message, "\nПункт правил 8: 🔥 Не заниматься расовым, религиозным или полит. розжигом. (свастика тоже запрещена). Также для одарённых, называть афроамериканца 'негр' - тоже расизм.Cледующий пункт правил /P9.\n")


@bot.message_handler(commands=['P9'])
def P9(message):
    bot.reply_to(message, "Пункт правил P9:В разработке.Cледующий пункт правил /P10 ")



@bot.message_handler(commands=['P10'])
def P10(message):
    bot.reply_to(message, "\nПункт правил 10:🔞Не присылать  стикеры 18+ Любой контент 18+ запрещён, даже иллюстрации из символов.Cледующий пункт правил /P11\n")


@bot.message_handler(commands=['P11'])
def P11(message):
    bot.reply_to(message, "\nПункт правил 11:©️Нельзя копировать акаунты администраторовCледующий пункт правил /P12.\n")


@bot.message_handler(commands=['P12'])
def P12(message):
    bot.reply_to(message, "\nПункт правил 12:👩‍👦Ни при каких условиях не трогать родителей и родных.Cледующий пункт правил /P13\n")


@bot.message_handler(commands=['P13'])
def P13(message):
    bot.reply_to(message, "\nПункт правил 13:💢❌Оскорбления и конфликты строго запрещены.Cледующий пункт правил /P14.\n")


@bot.message_handler(commands=['P14'])
def P14(message):
    bot.reply_to(message, "\nПункт правил 14:🙄Не надоедать администраторам.Cледующий пункт правил /P15.\n")


@bot.message_handler(commands=['P15'])
def P15(message):
    bot.reply_to(message, "\nПункт правил 15:💢💣запрещено отправлять то, из-за чего вылетает телеграм или взлом.Cледующий пункт правил /P16\n")


@bot.message_handler(commands=['P16'])
def P16(message):
    bot.reply_to(message, "\nПункт правил 16:🚯Запрещены нецензурные ники либо засоряющие чат.Cледующий пункт правил /P17.\n")


@bot.message_handler(commands=['P17'])
def P17(message):
    bot.reply_to(message, "\nПункт правил 17:Не надоедать разработчику по пустякам.Cледующий пункт правил /P18.\n")


@bot.message_handler(commands=['P18'])
def P18(message):
    bot.reply_to(message, "\nПункт правил 18:не шутить над администраторами(они могут  не понять что вы шутите и могут дать вам мут и вам будет не смешно)Cледующий пункт правил /P19.")


@bot.message_handler(commands=['P19'])
def P19(message):
    bot.reply_to(message, "\nПункт правил 19: не спамить боту в личные сообщения.Cледующий пункт правил /P20.")


@bot.message_handler(commands=['P20'])
def P19(message):
    bot.reply_to(message, "\nПока что на этом все.")



@bot.message_handler(commands=['ban'])
def ban_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Проверяем, является ли пользователь администратором чата
    if is_user_admin(chat_id, user_id):
        try:
            user_to_ban = message.reply_to_message.from_user.id
            bot.kick_chat_member(chat_id, user_to_ban)
            bot.reply_to(message, "Пользователь забанен.")
        except Exception as e:
            bot.reply_to(message, "Не удалось забанить пользователя.")
    else:
        bot.reply_to(message, "У вас нет прав для этой команды.")


# noinspection PyBroadException
@bot.message_handler(commands=['unban'])
def unban_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Проверяем, является ли пользователь администратором чата
    if is_user_admin(chat_id, user_id):
        try:
            user_to_unban = message.reply_to_message.from_user.id
            bot.unban_chat_member(chat_id, user_to_unban)
            bot.reply_to(message, "Пользователь разбанен.")
        except Exception as e:
            bot.reply_to(message, "Не удалось разбанить пользователя.")
    else:
        bot.reply_to(message, "У вас нет прав для этой команды.")


def is_user_admin(chat_id, user_id):
    chat_member = bot.get_chat_member(chat_id, user_id)
    return chat_member.status == "administrator" or chat_member.status == "creator"


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "\n1-я команда /kick-удаляет пользователя из группы.\n2-я команда /ban-блокирует и удаляет пользователя из группы.\n3-я команда /unban-обратная функция функции /ban.\n4-я команда Запрещает писать на определенное время(сколько назаначил администратор).\n5-я команда /unmute-обратная команда команде /mute.\n6-я функция показывает погоду в вашем городе по названию либо можно написать команду /weather .\n7-я функция - приветствие новых участников .\n8-я функция - фильтр против мата и плохих слов .\n9-я функция - запрещает отправлять стикеры в телеграмм.\n10-я команда /help-показывает список всех команд.\n11-я команда /start-ну тут я не вижу смысла объяснять.\n12-я команда для перехода в нейросеть Яндекса /YaGPT.\n13-я команда /yandex перейти в поисковик Яндекса.\n14-я команда /rules показывает правила чата(не изменяется).\n15-я команда /version показывает версию бота.\n16-команда 'рп команды' показывает список доступных РП команд.\n17-я команда /stats показывает статистику чата.\n18-я функция капчи.\n А на этом пока все.Будут новые функции. ")
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Your text", url="Your link")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Your text", reply_markup=keyboard)

@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно кикнуть администратора.")
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} был кикнут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите кикнуть.")


@bot.message_handler(commands=['mute'])
def mute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно замутить администратора.")
        else:
            duration = 60
            args = message.text.split()[1:]
            if args:
                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Неправильный формат времени.")
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 144000000000000000000000000000000000000000000000000000000000000000:
                    bot.reply_to(message, "Максимальное время - бесконечность день.")
                    return
            bot.restrict_chat_member(chat_id, user_id, until_date=time.time()+duration*60)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")


@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} размучен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")


@bot.message_handler(content_types=['text'])
def weather1i(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        lon = data['coord']['lon']
        lat = data['coord']['lat']
        max_temp = data['main']['temp_max']
        min_temp = data['main']['temp_min']
        nebo = data['weather'][0]['main']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        bot.reply_to(message, f"{time.strftime('%B %d, %Y')}\n"
              f"Погода в городе: {city}\nКоординаты объекта:\nШирота{lat}\nДолгота:{lon}\nТемпература: {temp}C°\nМаксимальная температура:{max_temp}° \nМинимальная температура: {min_temp}°C\nThe state of the sky:{nebo}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"\nХорошего дня! или вечера!\n"
              )

bad_words=["ссылка", "приглашение"]


def check_message(message):
    for word in bad_words:
        if word in message.text.lower():
            return True
    return False


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if check_message(message):
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"Пользователь {message.from_user.username} был удалени❌ или  заблокирован ⛔️за оскорбительные либо матерщинные сообщения")
    else:
        print(message.text)


bot.infinity_polling(none_stop=True)
