# -*- coding: iso-8859-1 -*-

import telebot
from telebot import types
import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import dht11
import datetime

TOKEN = '584192977:AAEZeAcqvXaCCOV2fz4Gf3edP4dDDxS3nM4'

knownUsers = []  # todo: save these in a file,

userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
              'start': 'Comenzar a usar el bot',
              'help': 'Informacion acerca de los comandos disponibles',
              'monitoreo_humedad_suelo': 'Monitoreo de la humedad del suelo',
              'monitoreo_humedad_ambiente': 'Monitoreo de la humedad del ambiente',
              'monitoreo_temperatura_ambiente': 'Monitoreo de la temperatura ambiente',
              'monitoreo_luz_uv': 'Monitoreo de la luz UV',
              'predicciones': 'Algunas recomendaciones Basicas',
}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
text=""
# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener

# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hola, extrano, permiteme escanearte...")
        bot.send_message(cid, "Escaneo completo, ahora te conozco")
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "Ya te conozco, no es necesario volver a escanearte!")

# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguientes comandos estan disponibles: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page

# Monitoreo humedad del suelo
@bot.message_handler(commands=['monitoreo_humedad_suelo'])
def command_monitoreo_humedad_suelo(m):
    cid = m.chat.id
    values = ((adc.read_adc(2, gain=GAIN)/34.7)/950)*100
    humedad = int(values)
    if humedad < 30:
        text = "El porcentaje de humedad en la tierra es de: " + str(humedad) + "% \n" + "Se recomienda regar el cultivo \n"
    elif humedad >= 30 and humedad < 60:
        text = "El porcentaje de humedad en la tierra es de: " + str(humedad) + "% \n" + " En las proximas horas la planta debera ser regada \n"
    else:
        text = "El porcentaje de humedad en la tierra es de: " + str(humedad) + "% \n" + " La planta no necesita ser regada \n"
    bot.send_message(cid, text)  # send the generated help page

# Monitoreo humedad ambiente
@bot.message_handler(commands=['monitoreo_humedad_ambiente'])
def command_monitoreo_humedad_ambiente(m):
    cid = m.chat.id
    instance = dht11.DHT11(pin=17)
    validacion = True
    while validacion:
        result = instance.read()
        if result.is_valid():
            humedad = int(result.humidity)
            validacion=False
    if humedad<50:
        text = "El valor de la humedad ambiente es : " + str(humedad) + "\n Estas en un ambiente seco "
    elif humedad >= 50 : 
        text = "El valor de la humedad ambiente es : " + str(humedad) + "\n Estas en un ambiente humedo"
    bot.send_message(cid, text)  # send the generated help page

# Monitoreo temperatura ambiente
@bot.message_handler(commands=['monitoreo_temperatura_ambiente'])
def command_monitoreo_temperatura_ambiente(m):
    cid = m.chat.id
    instance = dht11.DHT11(pin=17)
    validacion = True
    while validacion:
        result = instance.read()
        if result.is_valid():
            temperatura = int(result.temperature)
            validacion=False
    if temperatura<6:
        text = "El valor de la temperatura ambiente es : " + str(temperatura)  + "\n Estas en un ambiente frio tipo glacial"
    elif temperatura >= 6 and temperatura <12  :
        text = "El valor de la temperatura ambiente es : " + str(temperatura) + "\n Estas en un ambiente frio con valores cercanos a un paramo"
    elif temperatura >= 12 and temperatura <18  :
        text = "El valor de la temperatura ambiente es : " + str(temperatura) + "\n Estas en un ambiente frio "
    elif temperatura >= 18 and temperatura <24 : 
        text = "El valor de la temperatura ambiente es : " + str(temperatura) + "\n Estas en un ambiente templado"
    elif temperatura >=24 : 
        text = "El valor de la temperatura ambiente es : " + str(temperatura) + "\n Estas en un ambiente calido"
    bot.send_message(cid, text)  # send the generated help page

# Predicciones
@bot.message_handler(commands=['predicciones'])
def command_predicciones(m):
    cid = m.chat.id
    instance = dht11.DHT11(pin=17)
    validacion = True
    while validacion:
        result = instance.read()
        if result.is_valid():
            temperatura = int(result.temperature)
            humedadAire = int(result.humidity)
            validacion=False
    adc = Adafruit_ADS1x15.ADS1115()
    values = adc.read_adc(2, gain=GAIN)
    humedad = int(values)
    
    if humedadAire>80 and temperatura>13:
        text = "En este momento tenemos un alto porcentaje de humedad y una baja temperatura hay altas probabilidades de lluvia. Asi que aun no riegues tu planta" "\n"
    elif humedad<30 and temperatura>24:
        text = "¡Es un dia caluroso! \n Es hora de refrescar un poco tus plantas"
    elif humedad>50 and humedadAire>60 and temperatura<20:
        text = "¡Es un dia calido y seco! \n En este momento tu planta esta humedecida, esta en un ambiente genial"        
    elif humedad<30 and temperatura<14:
        text = "¡Es un dia frio! \n Es hora de refrescar un poco tus plantas"
    else:
        text="No tengo una recomendacion para ti en este momento"
    bot.send_message(cid, text)  # send the generated help page

# Monitoreo luz 
@bot.message_handler(commands=['monitoreo_luz_uv'])
def command_monitoreo_luz_uv(m):
    cid = m.chat.id
    adc = Adafruit_ADS1x15.ADS1115()
    values = adc.read_adc(3, gain=GAIN)
    uv = int(values)
    text = "El valor de la luz UV es : " + str(uv) + "\n"
    bot.send_message(cid, text)  # send the generated help page

bot.polling()
