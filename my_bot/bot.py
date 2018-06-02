# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import logging
from settings import constells_dict, TELEGRAM_API_KEY, PROXY
import ephem
import datetime
from datetime import time

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def start_handler(bot, update):
    """
    Обработчик команды /start
    """
    username = update.message.from_user.username
    bot_text = (
        'Привет {}. Для отображения списка команд /help .'.format(username))
    # update.message.reply_text(bot_text)
    bot.sendMessage(chat_id=update.message.chat.id, text=bot_text)


def planet_handler(bot, update):
    """
    обработчик команды /planet
    #/planet [Имя планеты] - выводит инфу о сегодня
    #/planet [Имя планеты] [дата] - выводит инфу за дату
    #/planet - выводит список всех планет в которые может ephem
    """
    now_time = datetime.datetime.now()
    ephem_date = now_time.strftime("%Y/%m/%d")
    user_text = update.message.text
    if user_text in ['/planet', '/planet@simple_astro_bot']:
        all_pl = '\n'.join('{}: {}'.format(value[1], value[2])
                           for value in ephem._libastro.builtin_planets()
                           if value[1].lower() == 'planet')
        bot_text = 'Список доступных планет:\n{}'.format(all_pl)
        bot.sendMessage(chat_id=update.message.chat.id, text=bot_text)
        return True
    # не очень ясно из задания, нужно перебрать КАЖДУЮ планету ifами??
    # это же не pythonic way :)
    splitted_msg = update.message.text.split(' ')
    # если длина списка больше двух, то меняем дату на указанную
    if len(splitted_msg) > 2:
        ephem_date = splitted_msg[2]
    planet_name = splitted_msg[1]
    try:
        planet_info = getattr(ephem, planet_name.capitalize())(ephem_date)
    except AttributeError:
        error_bot_msg = 'Такой планеты/спутника не найдено. Список /planet.'
        bot.sendMessage(chat_id=update.message.chat.id, text=error_bot_msg)
        return False
    except ValueError:
        error_bot_msg = 'Неверный формат даты. /help для помощи.'
        bot.sendMessage(chat_id=update.message.chat.id, text=error_bot_msg)
        return False
    # если всё ок то выводим о ней инфу
    short_term_planet_constell = ephem.constellation(planet_info)[0]
    ru_conts_name = constellations_translator(short_term_planet_constell)
    full_constell = '{}({})'.format(
        ephem.constellation(planet_info)[1], ru_conts_name)
    earth_dist_km = planet_info.earth_distance * 149600000
    bot_text = '{} находится в созвездии {}. Расстояние до земли: {} км. Дата: {}'.format(planet_name, full_constell,
                                                                                          earth_dist_km, ephem_date)
    bot.sendMessage(chat_id=update.message.chat.id, text=bot_text)


def help_handler(bot, update):
    """
    Функция обработчик команды /help
    Выводит список доступных команд с описанием
    """
    bot_text = """
    /help -
    /planet -
    /moon -
    /sun -
    /solar
    """
    bot.sendMessage(chat_id=update.message.chat.id, text=bot_text)


def moon_handler(bot, update):
    """
    Функция обработчик команды /moon
    """
    # получим текущее время
    now_time = datetime.datetime.now()
    ephem_date = now_time.strftime("%Y/%m/%d")
    # вытащим данные о луне
    growth_start_date = ephem.previous_new_moon(ephem_date)
    full_moon_date = ephem.next_full_moon(ephem_date)
    moon_info = ephem.Moon(ephem_date)
    # создадим из них строку
    bot_text = ('Луна растёт с {}\nПолнолуние наступит: {}\nЛуну видно на: {:.3f} %\nДистанция до земли: {:.3f} км.'
                .format(growth_start_date, full_moon_date, moon_info.moon_phase * 100, moon_info.earth_distance * 149600000))
    # напишем её в чатик
    bot.sendMessage(chat_id=update.message.chat.id, text=bot_text)


def solar_system_handler(bot, update):
    """
    обработчик команды /solar
    Тут отрисовываются объекты нашей солнечной системы(кнопками), на каждую из которых можно
    кликнуть и посмотреть инфу о ней на вики
    """
    solar_system = ['Солнце', 'Меркурий', 'Венера', 'Земля',
                    'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун',
                    'Плутон', 'Хаумеа', 'Макемаке', 'Эрида']
    url_buttons = [InlineKeyboardButton(text=item, url="https://ru.wikipedia.org/wiki/{}".format(item))
                   for item in solar_system]
    custom_keyboard = [url_buttons[:5], url_buttons[5:10], url_buttons[10:]]
    reply_markup = InlineKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat.id,
                     text="Выберите объект для изучения?",
                     reply_markup=reply_markup)


def sun_handler(bot, update):
    """
    Обработчик команды /sun
    Выводит инфу о солнце за сейчас
    """
    now_time = datetime.datetime.now()
    ephem_datetime = now_time.strftime("%Y/%m/%d %H:%M:%S")
    sun_info = ephem.Sun(ephem_datetime)
    # восход и закат по мск в этот день
    # расстояние до земли
    # задать обозревателья в Мск через ephem.city('Moscow') не получилось
    # непонятно почему, но тогда время восхода неверное(мб кроме horizon нужно больше параметров)
    # буду задавать обозревателя в мск по latitude
    moscow_obs = ephem.Observer()
    moscow_obs.lat = '51:28:38'
    moscow_obs.date = ephem_datetime
    previous_ris = moscow_obs.previous_rising(sun_info)
    previous_set = moscow_obs.previous_setting(sun_info)
    next_ris = moscow_obs.next_rising(sun_info)
    next_set = moscow_obs.next_setting(sun_info)
    earth_dist_km = sun_info.earth_distance * 149600000
    bot_text = """  В Москве({} ш.):
    Предыдущий восход: {}
    Предыдущий закат: {}
    Следующий восход: {}
    Следующий закат: {}
    Дистанция до земли: {:.3f} км.""".format(moscow_obs.lat, previous_ris, previous_set, next_ris, next_set, earth_dist_km)
    bot.sendMessage(chat_id=update.message.chat.id, text=bot_text)


def message_handler(bot, update):
    """
    Обработчик прямого текста к боту
    """
    #user_text = update.message.text
    # logging.info(user_text)
    username = update.message.from_user.username
    update.message.reply_text('@{} используй /help!'.format(username))


def strange_command_handler(bot, update):
    """
    Функция обрабатывающая странные команды
    Выводит подсказку, что можно ввести /help
    """
    bot_message = 'Не известная команда.\nИспользуйте /help для отображения списка команд.'
    update.message.reply_text(bot_message)


def constellations_translator(const_name):
    """
    Возвращает русское название по словарю созвезний или тоже самое, если нет в словаре
    """
    return constells_dict.get(const_name, const_name)


def main():
    updt = Updater(TELEGRAM_API_KEY, request_kwargs=PROXY)
    try:
        updt.start_polling()
    except Exception:
        print(';(')
        time.sleep(15)
# лучше отлавливать команды декораторами, наверное.
    updt.dispatcher.add_handler(CommandHandler("start", start_handler))
    updt.dispatcher.add_handler(CommandHandler("planet", planet_handler))
    updt.dispatcher.add_handler(CommandHandler("moon", moon_handler))
    updt.dispatcher.add_handler(CommandHandler("sun", sun_handler))
    updt.dispatcher.add_handler(CommandHandler("solar", solar_system_handler))
    updt.dispatcher.add_handler(CommandHandler("help", help_handler))
    updt.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    updt.dispatcher.add_handler(MessageHandler(
        Filters.command, strange_command_handler))
    updt.start_polling()
    updt.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()
