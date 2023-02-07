import telebot
from django.http import JsonResponse
from django.views import View
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot import types
import logging
from app.models import TgUser, Admin, Info
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import time


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

BOT_NAME = '@ProductUzBot'
bot = telebot.TeleBot('5875923517:AAHdupc3iddCYl-5XYQj79ZeCeU80cx28XU')



class BotAPIView(View):
    def post(self, request):
        json_string = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return JsonResponse({'code': 200})


@bot.message_handler(commands=['start'])
def process_start(message):
    bot.send_message(message.chat.id,
                           'Здравствуйте!\nПожалуйста, выберите язык\n\nAssalomu alaykum!\nIltimos, tilni tanlang')

