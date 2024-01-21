import telebot
from pytube import YouTube
import os
import random

bot = telebot.TeleBot("6789743997:AAHUVsgSi8B70sZJydLifRc7nMts06KwhtQ")


@bot.message_handler(commands = ("start"))
def start(message):
    bot.send_message(message.chat.id, """Привет! Это YouTuBot by mkhmtcore!😈\nЭтот бот предназначен для скачивания видео из ютуба. У бота не совсем много функционала, на то он и легкий!🥱\n\n\nСкидывай в этот чат ссылку из ютуба, и он тебе скачает это видео!😜\nУдачи тебе!😌""")

@bot.message_handler(commands = ['mkhmtcore', 'amina'])
def defline_who(message):
    bot.reply_to(message, "She is gf of Olzhas") if message.text == '/amina' else bot.reply_to(message, "He is creator of this bot")

@bot.message_handler(commands = ['test'])
def test(message):
    with open("B:/VS CODE/Telegramm bot/Скачанные видео/Dont Go Insane (DPR IAN) - best part loop.mp4", 'rb') as test:
        bot.send_video(message.chat.id, test)
        


@bot.message_handler(func = lambda message: "https://www.youtube.com" in message.text or "https://youtu.be" in message.text)
def downloading(message):
    bot.send_message(message.chat.id, "Видео скачивается...")
    number_name = random.randint(1, 1000000)
    try:
        youtube_video = YouTube(message.text)
        title = youtube_video.title.replace('.', '')
        title = title.replace("'", '')
        title = title.replace('|', '')
        output_path = "B:/VS CODE/Telegramm bot/Downloaded Videos/"

        youtube_video.streams.first().download(output_path=output_path)
        video_path = os.path.join(output_path, title + '.mp4')
        print(video_path)
        with open(video_path, 'rb') as video:
            bot.send_video(message.chat.id, video)
        os.remove(video_path)
        
        history_path = "B:/VS CODE/Telegramm bot/history.txt"
        with open(history_path, 'a') as history:
            history.write(f"{title}\n")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


bot.polling()