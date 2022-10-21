import Controller as con
from os import system

import User_interface as ui
import Loger as log
import breaking_data as bd
import Rational_math as rm
import Complex_math as cm
import Controller as con

import logging

from config import TOKEN

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot 
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    Handler
)

system ('cls')


                     
                        # Определяем константы этапов разговора
NUMBER, RATI, COMP, REPEAT_OR_END_CALC = range(4)



if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', con.start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            NUMBER: [MessageHandler(Filters.regex('^(Рациональные|Комплексные)$'), con.number)],
            RATI: [CommandHandler('cancel', con.cancel),MessageHandler(Filters.text, con.rac)],
            COMP: 
                [CommandHandler('cancel', con.cancel),MessageHandler(Filters.text, con.komp)],
            REPEAT_OR_END_CALC: 
                [MessageHandler(Filters.regex('^(Выход|Продолжить)$'), con.repeat_or_end_calc)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', con.cancel)],
    )


    message_handler=MessageHandler(Filters.text, con.give_word)
    unknown_handler = MessageHandler(Filters.command, con.unknown)


    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(unknown_handler)
    dispatcher.add_handler(message_handler)

    # Запуск бота
    log.log_data('|'+'-'*10+"Сервер старт"+'-'*10+'|')
    updater.start_polling()
    updater.idle()
    log.log_data('|'+'-'*10+"Сервер стоп"+'-'*10+'|'+'\n\n')