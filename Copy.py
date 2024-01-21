import telebot
from pytube import YouTube
import os

bot = telebot.TeleBot("6789743997:AAHUVsgSi8B70sZJydLifRc7nMts06KwhtQ")


@bot.message_handler(commands = ("start"))
def start(message):
    bot.send_message(message.chat.id, """Привет! Это YouTuBot by mkhmtcore!😈\nЭтот бот предназначен для скачивания видео из ютуба. У бота не совсем много функционала, на то он и легкий!🥱\n\n\nСкидывай в этот чат ссылку из ютуба, и он тебе скачает это видео!😜\nУдачи тебе!😌""")

@bot.message_handler(commands = ['mkhmtcore', 'amina'])
def defline_who(message):
    bot.reply_to(message, "She is gf of Olzhas") if message.text == '/amina' else bot.reply_to(message, "He is creator of this bot")

@bot.message_handler(func = lambda message: True if "https://www.youtube.com" or "https://youtu.be" in message.text else False)
def downloading(message):
    bot.send_message(message.chat.id, "Видео скачивается...")
    try:
        title = YouTube(message.text).title
        title = title.replace('.', '')
        print("B:/VS CODE/Telegramm bot/Скачанные видео/" + title + '.mp4')
        YouTube(message.text).streams.first().download(output_path = "B:/VS CODE/Telegramm bot/Скачанные видео")
        with open("B:/VS CODE/Telegramm bot/Скачанные видео/" + title + '.mp4', 'rb') as video:
            bot.send_video(message.chat.id, video)

        try:
            os.remove("B:/VS CODE/Telegramm bot/Скачанные видео/" + title + '.mp4')
        except Exception:
            None
    except Exception:
        bot.send_message(message.chat.id, "Скачать не получилось")

    


# @bot.message_handler(func = lambda message: True if "mkhmtcore" in message.text.rstrip("?").lower().split() else False)
# def defline_Asanali(message):
#     bot.reply_to(message, "He is creator of this bot")





bot.polling()