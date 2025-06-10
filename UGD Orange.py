from telebot import TeleBot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
import os
import sys
import platform
import requests
import pymorphy3
from datetime import datetime
import logging
from pyTelegramBotCAPTCHA import CaptchaManager
import datetime



bot = TeleBot('')
API = ''
morph = pymorphy3.MorphAnalyzer()
captcha_manager = CaptchaManager(bot)


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



@bot.message_handler(func=lambda message: message.text.lower() == "расстрелять")
def nas(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🔫|{tag1} расстрелял(-а) {tag2}', parse_mode='markdown')


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
    bot.reply_to(message, f'👊|{tag1} ударил(-а) {tag2}', parse_mode='markdown')


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


@bot.message_handler(func=lambda message: message.text.lower() == "выебать")
def command_text_privекеее(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'|{tag1} жестоко надругался в постеле над {tag2}', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "изнасиловать")
def command_text_nasil(message):
    tag2 = f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})"
    tag1 = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.reply_to(message, f'🔞|{tag1} изнасиловал(-а) {tag2} в постеле.', parse_mode='markdown')


@bot.message_handler(func=lambda message: message.text.lower() == "поприветствовать")
def command_text_kkkk(message):
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


def format_weather(city, data):
    # Склонение города
    parsed = morph.parse(city)[0]
    city_locative = parsed.inflect({'loct'})
    city_name = city_locative.word.capitalize() if city_locative else city.title()

    weather_desc = data['weather'][0]['description'].capitalize()
    temp = round(data['main']['temp'])
    feels_like = round(data['main']['feels_like'])
    temp_min = round(data['main']['temp_min'])
    temp_max = round(data['main']['temp_max'])
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    visibility = data.get('visibility', 0) // 1000
    cloudiness = data['clouds']['all']
    wind_speed = data['wind']['speed']
    wind_deg = data['wind'].get('deg', 0)

    sunrise_ts = data['sys']['sunrise']
    sunset_ts = data['sys']['sunset']
    timezone_offset = data['timezone']
    sunrise = datetime.utcfromtimestamp(sunrise_ts + timezone_offset).strftime('%H:%M')
    sunset = datetime.utcfromtimestamp(sunset_ts + timezone_offset).strftime('%H:%M')

    wind_dirs = ['северный', 'северо-восточный', 'восточный', 'юго-восточный', 'южный', 'юго-западный', 'западный', 'северо-западный']
    wind_dir = wind_dirs[round(wind_deg % 360 / 45) % 8]

    reply = (
        f"**🌍 Погода в {city_name}:**\n\n"
        f"📝 Состояние: *{weather_desc}*\n"
        f"🌡 Температура: *{temp}°C* (ощущается как *{feels_like}°C*)\n"
        f"🔻 Минимум: *{temp_min}°C* | 🔺 Максимум: *{temp_max}°C*\n"
        f"💧 Влажность: *{humidity}%*\n"
        f"🔽 Давление: *{pressure} гПа*\n"
        f"🌫 Видимость: *{visibility} км*\n"
        f"☁️ Облачность: *{cloudiness}%*\n"
        f"🌬 Ветер: *{wind_speed} м/с*, {wind_dir}\n"
        f"🌅 Восход: *{sunrise}* | 🌇 Закат: *{sunset}*\n\n"
        f"[🗺 Открыть карту погоды](https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat={data['coord']['lat']}&lon={data['coord']['lon']}&zoom=10)"
    )
    return reply

@bot.message_handler(commands=['weather'])
def get_weather(message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        bot.reply_to(message, "❌ Укажите город: /weather <город>")
        return

    city = args[1].strip()
    send_weather(message.chat.id, city)

def send_weather(chat_id, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            bot.send_message(chat_id, "❌ Город не найден или ошибка при получении данных.")
            return

        data = response.json()
        text = format_weather(city, data)

        markup = types.InlineKeyboardMarkup()
        refresh_btn = types.InlineKeyboardButton("🔄 Обновить", callback_data=f"refresh_weather:{city}")


        markup.add(refresh_btn)

        bot.send_message(chat_id, text, parse_mode='Markdown', reply_markup=markup)

    except Exception as e:
        bot.send_message(chat_id, f"⚠️ Ошибка:\n`{e}`", parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith("refresh_weather:"))
def refresh_weather(call):
    city = call.data.split(":", 1)[1]
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
        print(f"❌ Не удалось удалить сообщение: {e}")

    send_weather(call.message.chat.id, city)


@bot.message_handler(commands=['help'])
def help_command(message):
    send_help_menu(message.chat.id)

def send_help_menu(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("🚫 /kick", callback_data="help_kick"),
        InlineKeyboardButton("🔨 /ban", callback_data="help_ban"),
        InlineKeyboardButton("♻ /unban", callback_data="help_unban"),
        InlineKeyboardButton("⚠ /warn", callback_data="help_warn"),
        InlineKeyboardButton("🔇 /mute", callback_data="help_mute"),
        InlineKeyboardButton("🔊 /unmute", callback_data="help_unmute")
    )

    help_text = (
        "📚 *Справка по командам бота:*\n\n"
        "Нажми на одну из кнопок ниже, чтобы получить описание команды."
    )

    bot.send_message(chat_id, help_text, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("help_") or call.data == "help_back")
def help_callback(call):
    commands_info = {
        "kick": "🚫 *Команда /kick*\n\nИсключает пользователя из чата. Только для администраторов.",
        "ban": "🔨 *Команда /ban*\n\nНавсегда блокирует пользователя. Он не сможет вернуться в чат.",
        "unban": "♻ *Команда /unban*\n\nСнимает бан, позволяя пользователю вернуться.",
        "warn": "⚠ *Команда /warn*\n\nВыдаёт предупреждение. Полезно для системы нарушений.",
        "mute": "🔇 *Команда /mute*\n\nЗапрещает пользователю писать сообщения.",
        "unmute": "🔊 *Команда /unmute*\n\nСнимает ограничения, наложенные /mute.",
    }

    if call.data == "help_back":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        send_help_menu(call.message.chat.id)
        bot.answer_callback_query(call.id)
        return

    command_key = call.data.replace("help_", "")
    if command_key in commands_info:
        text = commands_info[command_key]
        back_markup = InlineKeyboardMarkup()
        back_markup.add(InlineKeyboardButton("◀ Назад", callback_data="help_back"))

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=text,
            parse_mode="Markdown",
            reply_markup=back_markup
        )
        bot.answer_callback_query(call.id)



@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user = message.from_user
    user_mention = f"[{user.first_name}](tg://user?id={user.id})"
    is_private = message.chat.type == "private"

    try:
        bot.delete_message(chat_id, message.message_id)
    except:
        pass

    if is_private:
        greeting_text = (
            f"👋 Привет, {user_mention}!\n\n"
            "Добро пожаловать в *BotGDX Moderator* — универсального помощника по модерации и автоматизации чатов.\n\n"
            "🔍 Чтобы узнать мои возможности, введи команду `/help`\n"
            "📦 Чтобы добавить меня в группу — нажми кнопку ниже.\n\n"
            "📢 [Новостной канал](https://t.me/BotGDM)\n"
            "🛡 [Логи модерации](https://t.me/BotGD_Moderator_log)"
        )

        invite_btn = InlineKeyboardMarkup()
        invite_btn.add(
            InlineKeyboardButton("➕ Добавить в группу", url=f"https://t.me/{bot.get_me().username}?startgroup=true")
        )

        bot.send_message(
            chat_id,
            greeting_text,
            parse_mode="Markdown",
            reply_markup=invite_btn
        )

    else:
        group_greeting = (
            f"✅ {user_mention}, бот успешно активирован в этом чате!\n\n"
            "🔧 Используй `/help`, чтобы ознакомиться с командами.\n"
            "⚙️ Я готов защищать ваш чат и помогать с управлением!"
        )

        bot.send_message(chat_id, group_greeting, parse_mode="Markdown")

    log_message = (
        f"📥 Команда /start\n"
        f"👤 Пользователь: {user_mention} (`{user.id}`)\n"
        f"💬 Тип чата: {message.chat.type}\n"
        f"🕓 Серверное время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    log_filename = f"logs/{message.chat.title or user.username or 'private'}_{chat_id}start.log"
    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(log_message + "\n\n")


start_time = time.time()

def format_uptime():
    seconds = int(time.time() - start_time)
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days}д {hours}ч {minutes}м {seconds}с"

def get_last_reboot_time():
    return datetime.datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")

@bot.message_handler(commands=["status"])
def status_handler(message):
    chat = message.chat
    user = message.from_user
    members = bot.get_chat_members_count(chat.id)

    chat_type = {
        "private": "Личное сообщение",
        "group": "Группа",
        "supergroup": "Супергруппа",
        "channel": "Канал"
    }.get(chat.type, "Неизвестно")

    bot_info = bot.get_me()

    text = (
    f"🛰️ <b>Статус бота</b>\n\n"
    f"👤 <b>Пользователь:</b> {user.first_name} (ID: <code>{user.id}</code>)\n"
    f"🆔 <b>Чат:</b> {chat.title or 'ЛС'} (ID: <code>{chat.id}</code>)\n"
    f"💬 <b>Тип чата:</b> {chat_type}\n"
    f"👥 <b>Участников:</b> {members}\n\n"
    f"🤖 <b>Бот:</b> {bot_info.first_name} (@{bot_info.username})\n"
    f"🧠 <b>Версия:</b> beta-2025.1.0, доступные изменения: <a href='https://github.com/qlswe/UGD_Yellow/commit/7292470fe8ff7ab68bae4912ffc95e080e0c19e5'>*тык*</a>\n"
    f"⚙️ <b>Python:</b> {platform.python_version()}\n\n"
    f"⏱ <b>Аптайм:</b> {format_uptime()}\n"
    f"🔁 <b>Последний запуск:</b> {get_last_reboot_time()}\n"
    f"🕒 <b>Время на сервере:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    bot.send_message(chat.id, text, parse_mode="HTML")


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_action(chat, initiator, target, action):
    chat_title = chat.title if chat.title else str(chat.id)
    log_filename = os.path.join(LOG_DIR, f"{chat_title}.log")
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now()}] {initiator.first_name} ({initiator.id}) → "
                       f"{action} {target.first_name} ({target.id})\n")

@bot.message_handler(commands=['promote'])
def promote_user(message):
    if not message.reply_to_message:
        bot.reply_to(message, "❌ Ответьте на сообщение пользователя, чтобы назначить его администратором.")
        return

    chat_id = message.chat.id
    initiator = message.from_user
    target = message.reply_to_message.from_user

    if not is_user_admin(chat_id, initiator.id):
        bot.reply_to(message, "🚫 У вас нет прав для назначения администраторов.")
        return

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Полные", callback_data=f"promote_full:{chat_id}:{target.id}:{initiator.id}"),
        types.InlineKeyboardButton("Модератор", callback_data=f"promote_restrict:{chat_id}:{target.id}:{initiator.id}"),
        types.InlineKeyboardButton("Только закрепление", callback_data=f"promote_pin:{chat_id}:{target.id}:{initiator.id}")
    )
    bot.reply_to(message, f"🔧 Выберите режим повышения для {target.first_name}:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("promote_"))
def handle_promote_callback(call):
    parts = call.data.split(":")
    mode, chat_id, target_id, initiator_id = parts[0].replace("promote_", ""), int(parts[1]), int(parts[2]), int(parts[3])

    if call.from_user.id != initiator_id:
        bot.answer_callback_query(call.id, "⛔ Только отправитель команды может выбрать режим.")
        return

    perms = {
        "full": dict(
            can_change_info=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=False
        ),
        "restrict": dict(
            can_change_info=False,
            can_delete_messages=True,
            can_invite_users=False,
            can_restrict_members=True,
            can_pin_messages=False,
            can_promote_members=False
        ),
        "pin": dict(
            can_change_info=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=True,
            can_promote_members=False
        )
    }

    try:
        bot.promote_chat_member(chat_id, target_id, **perms[mode])
        bot.edit_message_text(
            f"✅ Пользователь [ID:{target_id}](tg://user?id={target_id}) назначен администратором в режиме *{mode}*.",
            chat_id, call.message.message_id, parse_mode="Markdown"
        )
        log_action(call.message.chat, call.from_user, types.User(id=target_id, first_name="Пользователь"), f"PROMOTE ({mode})")
    except Exception as e:
        bot.edit_message_text(f"⚠️ Не удалось выдать права.\nОшибка: {e}", chat_id, call.message.message_id)

@bot.message_handler(commands=['demote'])
def demote_user(message):
    if not message.reply_to_message:
        bot.reply_to(message, "❌ Ответьте на сообщение пользователя, чтобы снять его с администраторов.")
        return

    chat_id = message.chat.id
    initiator = message.from_user
    target = message.reply_to_message.from_user

    if not is_user_admin(chat_id, initiator.id):
        bot.reply_to(message, "🚫 У вас нет прав для снятия администраторов.")
        return

    try:
        member = bot.get_chat_member(chat_id, target.id)
        if member.status == "creator":
            bot.reply_to(message, "❗ Нельзя снять с должности владельца чата.")
            return

        bot.promote_chat_member(chat_id, target.id,
            can_change_info=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False
        )
        bot.reply_to(message,
            f"ℹ️ [{target.first_name}](tg://user?id={target.id}) больше не является администратором.",
            parse_mode="Markdown"
        )
        log_action(message.chat, initiator, target, "DEMOTE")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Не удалось снять администратора.\nОшибка: {e}")


def setup_logger(chat):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    filename = f"{chat.title or chat.id}administrator.log".replace(" ", "_")
    log_path = os.path.join(log_dir, filename)
    logger = logging.getLogger(str(chat.id))
    if not logger.handlers:
        handler = logging.FileHandler(log_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger

def is_user_admin(chat_id, user_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["administrator", "creator"]
    except Exception as e:
        return False

@bot.message_handler(commands=['ban', 'запрет'])
def ban_user(message):
    logger = setup_logger(message.chat)
    if not is_user_admin(message.chat.id, message.from_user.id):
        return bot.reply_to(message, "❌ Нет прав.")
    if not message.reply_to_message:
        return bot.reply_to(message, "⚠️ Ответьте на сообщение пользователя.")

    user_id = message.reply_to_message.from_user.id
    if is_user_admin(message.chat.id, user_id):
        return bot.reply_to(message, "🛡️ Нельзя банить админа.")
    try:
        bot.kick_chat_member(message.chat.id, user_id)
        logger.info(f"{message.from_user.username} забанил {message.reply_to_message.from_user.username} ({user_id})")
        bot.reply_to(message, "✅ Пользователь забанен.")
    except Exception as e:
        logger.error(f"Ошибка при бане: {e}")
        bot.reply_to(message, "❌ Ошибка при бане.")

@bot.message_handler(commands=['kick', 'выпнуть'])
def kick_user(message):
    logger = setup_logger(message.chat)
    if not is_user_admin(message.chat.id, message.from_user.id):
        return bot.reply_to(message, "❌ Нет прав.")
    if not message.reply_to_message:
        return bot.reply_to(message, "⚠️ Ответьте на сообщение пользователя.")
    user_id = message.reply_to_message.from_user.id
    if is_user_admin(message.chat.id, user_id):
        return bot.reply_to(message, "🛡️ Нельзя кикать админа.")
    try:
        bot.kick_chat_member(message.chat.id, user_id)
        bot.unban_chat_member(message.chat.id, user_id)  # чтобы не остался забаненным
        logger.info(f"{message.from_user.username} кикнул {message.reply_to_message.from_user.username} ({user_id})")
        bot.reply_to(message, "✅ Пользователь кикнут.")
    except Exception as e:
        logger.error(f"Ошибка при кике: {e}")
        bot.reply_to(message, "❌ Ошибка при кике.")

@bot.message_handler(commands=['mute', 'мут', 'тишина'])
def mute_user(message):
    logger = setup_logger(message.chat)
    if not is_user_admin(message.chat.id, message.from_user.id):
        return bot.reply_to(message, "❌ Нет прав.")
    if not message.reply_to_message:
        return bot.reply_to(message, "⚠️ Ответьте на сообщение пользователя.")

    user_id = message.reply_to_message.from_user.id
    if is_user_admin(message.chat.id, user_id):
        return bot.reply_to(message, "🛡️ Нельзя мутить админа.")

    args = message.text.split()
    duration = 10
    if len(args) > 1:
        try:
            duration = int(args[1])
        except ValueError:
            return bot.reply_to(message, "❌ Неверный формат времени. Пример: /mute 5")
    until = int(time.time() + duration * 60)
    try:
        bot.restrict_chat_member(
            message.chat.id,
            user_id,
            until_date=until,
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False
        )
        logger.info(f"{message.from_user.username} замутил {message.reply_to_message.from_user.username} ({user_id}) на {duration} минут.")
        bot.reply_to(message, f"🔇 Пользователь замучен на {duration} минут.")
    except Exception as e:
        logger.error(f"Ошибка при муте: {e}")
        bot.reply_to(message, "❌ Ошибка при муте.")

@bot.message_handler(commands=['unmute', 'размут'])
def unmute_user(message):
    logger = setup_logger(message.chat)
    if not is_user_admin(message.chat.id, message.from_user.id):
        return bot.reply_to(message, "❌ Нет прав.")
    if not message.reply_to_message:
        return bot.reply_to(message, "⚠️ Ответьте на сообщение пользователя.")
    user_id = message.reply_to_message.from_user.id
    try:
        bot.restrict_chat_member(
            message.chat.id,
            user_id,
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True
        )
        logger.info(f"{message.from_user.username} размутил {message.reply_to_message.from_user.username} ({user_id})")
        bot.reply_to(message, f"🔈 Пользователь размучен.")
    except Exception as e:
        logger.error(f"Ошибка при размуте: {e}")
        bot.reply_to(message, "❌ Ошибка при размуте.")

@bot.message_handler(commands=['unban', 'разбан'])
def unban_user(message):
    logger = setup_logger(message.chat)
    if not is_user_admin(message.chat.id, message.from_user.id):
        return bot.reply_to(message, "❌ Нет прав.")
    if not message.reply_to_message:
        return bot.reply_to(message, "⚠️ Ответьте на сообщение пользователя.")
    user_id = message.reply_to_message.from_user.id
    try:
        bot.unban_chat_member(message.chat.id, user_id)
        logger.info(f"{message.from_user.username} разбанил {message.reply_to_message.from_user.username} ({user_id})")
        bot.reply_to(message, f"✅ Пользователь разбанен.")
    except Exception as e:
        logger.error(f"Ошибка при разбане: {e}")
        bot.reply_to(message, "❌ Ошибка при разбане.")

@bot.message_handler(commands=['del', 'удалить'])
def deletlle_message(message):
    logger = setup_logger(message.chat)
    if not is_user_admin(message.chat.id, message.from_user.id):
        return bot.reply_to(message, "❌ Нет прав.")
    if not message.reply_to_message:
        return bot.reply_to(message, "⚠️ Ответьте на сообщение, которое нужно удалить.")
    try:
        bot.delete_message(message.chat.id, message.reply_to_message.message_id)
        logger.info(f"{message.from_user.username} удалил сообщение {message.reply_to_message.message_id} от {message.reply_to_message.from_user.username}")
        bot.reply_to(message, "🗑 Сообщение удалено.")
    except Exception as e:
        logger.error(f"Ошибка при удалении: {e}")
        bot.reply_to(message, "❌ Ошибка при удалении.")


if __name__ == "__main__":
    print("Bot is polling...")
    bot.polling(none_stop=True)
