import telebot
from config import TOKEN
from logic import tran, text_recognition

bot = telebot.TeleBot(TOKEN)

dest = 'en'


@bot.message_handler(commands=['help', 'start'])
def handle_docs_photo(message):
    bot.send_message(message.chat.id, 'отправьте текст и получите перевод, можете поменять язык командой /lang [код языка].')

@bot.message_handler(commands=['lang'])
def handle_docs_photo(message):
    global dest
    dest = message.text.split()[1]
    bot.send_message(message.chat.id, f'вы сменили язык перевода на {dest}.')

# @bot.message_handler(commands=['dst'])
# def handle_docs_photo(message):
#     print(dest)
#     print(tran('привет мир', dest))

@bot.message_handler(content_types=['text'])
def handle_docs_photo(message):
    bot.send_message(message.chat.id, tran(message.text, dest))

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    print(file_name)
    text = text_recognition(file_path=file_name)
    result = tran(text, dest)
    bot.send_message(message.chat.id, result)



bot.infinity_polling()