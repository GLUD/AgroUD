import telebot
from telebot import types
import time

TOKEN = '584192977:AAEZeAcqvXaCCOV2fz4Gf3edP4dDDxS3nM4'

knownUsers = []  # todo: save these in a file,

userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
              'start': 'Comenzar a usar el bot',
              'help': 'Información acerca de los comandos disponibles',
}

# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener

# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hola, extraño, permiteme escanearte...")
        bot.send_message(cid, "Escaneo completo, ahora te conozco")
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "Ya te conozco, no es necesario volver a escanearte!")

# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguientes comandos están disponibles: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page

bot.polling()
