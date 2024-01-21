import telebot
from pytube import YouTube
import os

bot = telebot.TeleBot("6789743997:AAHUVsgSi8B70sZJydLifRc7nMts06KwhtQ")


@bot.message_handler(commands = ("start"))
def start(message):
    bot.send_message(message.chat.id, "Привет")

@bot.message_handler(func = lambda message: True if "https://www.youtube.com" or "https://youtu.be" in message.text else False)
def downloading(message):
    bot.send_message(message.chat.id, "Видео скачивается...")
    try:
        title = YouTube(message.text).title
        print("B:/VS CODE/Telegramm bot/Скачанные видео/" + title + '.mp4')
        YouTube(message.text).streams.first().download(output_path = "B:/VS CODE/Telegramm bot/Скачанные видео")
        with open("B:/VS CODE/Telegramm bot/Скачанные видео/" + title + '.mp4', 'rb') as video:
            bot.send_video(message.chat.id, video)

        try:
            os.remove("B:/VS CODE/Telegramm bot/Скачанные видео/" + title + '.mp4')
        except Exception:
            pass
    except Exception:
        bot.send_message(message.chat.id, "Скачать не получилось")

    

@bot.message_handler(func = lambda message: True if "amina" in message.text.rstrip("?").lower().split() else False)
def defline_Amina(message):
    bot.reply_to(message, "She is gf of Olzhas")

@bot.message_handler(func = lambda message: True if "mkhmtcore" in message.text.rstrip("?").lower().split() else False)
def defline_Asanali(message):
    bot.reply_to(message, "He is creator of this bot")





bot.polling()