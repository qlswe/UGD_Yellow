from telebot import TeleBot
from pyTelegramBotCAPTCHA import CaptchaManager
import time
from telebot import types
import requests
import json
import psutil
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = TeleBot('TOKEN_BOTFATHER')
API = 'TOKEN_OPENWEATHER'
captcha_manager = CaptchaManager(bot.get_me().id)



#@bot.message_handler(func=lambda message: True, content_types=['sticker'])
#def handle_sticker(msg):
    #bot.delete_message(msg.chat.id, msg.message_id)
    #bot.send_message(msg.chat.id, "⚠️️все стикеры блокируются кодом")



@bot.message_handler(commands=['report'])
def handle_report(message):
    if message.reply_to_message is None:
        bot.send_message(message.chat.id, 'Пожалуйста, ответьте на сообщение, чтобы отправить репорт.')
    else:
        report_message = message.reply_to_message
        report_message_link = f"https://t.me/{message.chat.username}/{report_message.message_id}"
        bot.send_message('ID_ADMIN',f'Новый репорт на сообщение пользователя: {report_message_link}\nПричина: {message.text.split(" ", 1)[1]}')
        bot.send_message(message.chat.id, 'Админы оповещены!')


@bot.message_handler(func=lambda message: message.text.lower() == "расстрелять")
def nas(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🔫|{tag1} расстрелял(-а) {tag2}', parse_mode='markdown')


# Message handler for new chat members
@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
  for new_user in message.new_chat_members:
    captcha_manager.restrict_chat_member(bot, message.chat.id, new_user.id)
    captcha_manager.send_new_captcha(bot, message.chat, new_user)

# Callback query handler
@bot.callback_query_handler(func=lambda callback:True)
def on_callback(callback):
  captcha_manager.update_captcha(bot, callback)

#Handler for correct solved CAPTCHAs
@captcha_manager.on_captcha_correct
def on_correct(captcha):
  bot.send_message(captcha.chat.id, "Congrats! You solved the CAPTCHA!")
  captcha_manager.unrestrict_chat_member(bot, captcha.chat.id, captcha.user.id)
  captcha_manager.delete_captcha(bot, captcha)

# Handler for wrong solved CAPTCHAs
@captcha_manager.on_captcha_not_correct
def on_not_correct(captcha):
  if (captcha.incorrect_digits == 1 and captcha.previous_tries < 2):
    captcha_manager.refresh_captcha(bot, captcha)
  else:
    bot.kick_chat_member(captcha.chat.id, captcha.user.id)
    bot.send_message(captcha.chat.id, f"{captcha.user.first_name} failed solving the CAPTCHA and was banned!")
    captcha_manager.delete_captcha(bot, captcha)

# Handler for timed out CAPTCHAS
@captcha_manager.on_captcha_timeout
def on_timeout(captcha):
  bot.kick_chat_member(captcha.chat.id, captcha.user.id)
  bot.send_message(captcha.chat.id, f"{captcha.user.first_name} did not solve the CAPTCHA and was banned!")
  captcha_manager.delete_captcha(bot, captcha)


@bot.message_handler(func=lambda message: message.text.lower() == "покормить")
def eda(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🥄|{tag1} тебя покрмил(-а) с ложочки {tag2} ', parse_mode='markdown')


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
    bot.reply_to(message, f'👅️|{tag1} отсосал(-а) у {tag2} ', parse_mode='markdown')


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


@bot.message_handler(func=lambda message: message.text.lower() == "отлизать")
def sosif(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'👅|{tag1} Отлизал у {tag2}',  parse_mode='markdown')


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


@bot.message_handler(func=lambda message: message.text.lower() == "въебать")
def sossss(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🤕|{tag1}Въебал(-а) со всей силы {tag2}',  parse_mode='markdown')



@bot.message_handler(func=lambda message: message.text.lower() == "рп команды")
def rpcom(message):
    bot.send_message(message.chat.id, "Список доступных РП команд: \n1)Поприветствовать.\n2)запереть.\n3)обнять.\n4)попращаться.\n5)попить чай.\n6)утопить.\n7)убить.\n8)расстрелять.\n9)отсосать.\n10)поприветствовать.\n11)утопить.\n12)погладить.\n13)покормить.\n14)похоронить.\n15)поцеловать.")

# обработчик команды /stats
@bot.message_handler(commands=['stats'])
def send_stats(message):
    bot_info = bot.get_me()
    subscribers = bot.get_chat_members_count(message.chat.id)
    text = f'Bot Name: {bot_info.first_name}\nUsername: @{bot_info.username}\nSubscribers:{subscribers}'
    bot.send_message(message.chat.id, text)



@bot.message_handler(commands=['version'])
def version(message):
   bot.reply_to(message, 'python version: 3.10 Version bot:2.1 changes:[#f7d632a](https://github.com/qlswe/UGD_Yellow2.0/commit/f7d632a07bb6f637992c7ca8da92b0306a5eb7c8)', parse_mode='Markdown')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKFNJk4h9cKutDx33CspIddPVgidb4mwACfBIAAvGYMUunL614YVTCCDAE")
    bot.reply_to(message, "Привет! Я бот для управления чатом. Напиши /help, чтобы начать использование и узнать, что я умею.\n\n[🗞Новостной канал бота.](https://t.me/ugd_dev)\n\n[🔐Канал с логами бота.](https://t.me/ugd_log)", parse_mode='Markdown')
    chat_id = message.chat.id
    button_text = "Добавить бота в чат"
    button_url = f"https://telegram.me/{bot.get_me().username}?startgroup=true"
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(InlineKeyboardButton(text=button_text, url=button_url))
    bot.send_message(chat_id,  "Нажмите кнопку, чтобы добавить бота в чат", reply_markup=inline_keyboard)


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
    bot.reply_to(message, f"Состояние системы в данный момент:\n{sys_status}")


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


@bot.message_handler(commands=['yandex'])
def yandex(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Yandex", url="https://yandex.ru/")
    keyboard.add(url_button)
    bot.send_photo(message.chat.id, "https://cdn-st2.rtr-vesti.ru/vh/pictures/hd/160/365/7.jpg")
    bot.send_message(message.chat.id, "Иши сколько угодно:_)", reply_markup=keyboard)


@bot.message_handler(commands=['off'])
def off(message):
    bot.reply_to(message, "Выключение...")
    bot.reply_to(message, "Если захотите снова включить сделайте это через консоль сервра.")
    bot.reply_to(message, "Готово☑️")
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time()+86400)
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
def P20(message):
    bot.reply_to(message, "\nПока что на этом все.")

@bot.message_handler(commands=['whoami'])
def whoami(message):

    # Получаем ID пользователя
    user_id = message.from_user.id

    # Получаем информацию о пользователе
    user_info = bot.get_chat_member(chat_id=message.chat.id, user_id=user_id)

    # Получаем имя пользователя
    user_name = user_info.user.first_name
    if user_info.user.last_name is not None:
        user_name += ' '+user_info.user.last_name

    # Отвечаем на запрос
    bot.send_message(message.chat.id, f'Вы {user_name} ({user_id})')

@bot.message_handler(commands=['ban', 'бан'])
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
    bot.reply_to(message, "\nкоманда /kick-удаляет пользователя из группы.\n команда /ban-блокирует и удаляет пользователя из группы.\nкоманда /unban-обратная функция функции /ban.\n команда Запрещает писать на определенное время(сколько назаначил администратор).\nкоманда /unmute-обратная команда команде /mute.\nфункция показывает погоду в вашем городе по названию либо можно написать команду /weather.\nфункция - приветствие новых участников .\nфункция - фильтр против мата и плохих слов .\nфункция - запрещает отправлять стикеры в телеграмм.\nкоманда /help-показывает список всех команд.\nкоманда /start-ну тут я не вижу смысла объяснять.\nкоманда для перехода в нейросеть Яндекса /YaGPT.\nкоманда /yandex перейти в поисковик Яндекса.\nкоманда /rules показывает правила чата(не изменяется).\nкоманда /version показывает версию бота.\nкоманда 'рп команды' показывает список доступных РП команд.\nкоманда /stats показывает статистику чата.\nфункция капчи.\n А на этом пока все.Будут новые функции. ")
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Жми сюда", url="https://ugdblog.my1.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Посетить мой блог.", reply_markup=keyboard)

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


@bot.message_handler(commands=['mute', 'мут', 'Мут', 'warn'])
def muter_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно замутить администратора.")
        else:
            duration = 60 # Значение по умолчанию - 1 минута
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
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} замучен 🤐 на {duration} минут за нарушение правил.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")



@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} размучен.Но в следующий раз лучше следить за языком.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")


@bot.message_handler(commands=['weather'])
def get_weather(message):
    bot.send_message(message.chat.id, 'Введите название города:')


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

        bot.reply_to(message, f"{time.strftime('%B %d, %Y')}🗓\n"
              f"\nПогода в городе: {city}\n\nКоординаты объекта:\nШирота{lat}\nДолгота:{lon}\n\nТемпература: {temp}C°🌡\nМаксимальная температура:{max_temp}C°🥵 \nМинимальная температура: {min_temp}°C🥶\n\nThe state of the sky:{nebo}\n"
              f"Влажность: {humidity}%💦\nДавление: {pressure} мм.рт.ст😶‍🌫️\nВетер: {wind} м/с💨\n\n"
              f"Восход солнца: {sunrise_timestamp}🌅\nЗакат солнца: {sunset_timestamp}🌆\nПродолжительность дня: {length_of_the_day}☀️\n\n"
              f"\nХорошего дня! или вечера!🍀"
              )


bad_words = ['Плохое_слово']


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

