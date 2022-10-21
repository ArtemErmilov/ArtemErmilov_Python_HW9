import User_interface as ui
import Loger as log
import breaking_data as bd
import Rational_math as rm
import Complex_math as cm
import Controller as con

import logging



from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot 
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    Handler
)

                        # Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


NUMBER, RATI, COMP, REPEAT_OR_END_CALC = range(4)

def repeat_or_end_calc_menu (update):
    reply_keyboard = [['Выход', 'Продолжить']]
    
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    
    update.message.reply_text(
        'Продолжить работу калькулятора, или выйти?',
        reply_markup=markup_key,)

def start(update, _):
    user = update.message.from_user
    logger.info("Старт бот-калькулятор. Пользователь %s %s", user.first_name, user.last_name)
    log.log_data(f"Старт бот-калькулятор. Пользователь {user.first_name} {user.last_name} ")

    reply_keyboard = [['Рациональные', 'Комплексные']]
    
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    
    update.message.reply_text(
        f'Приветствую тебя {user.first_name} {user.last_name}\n'
        'Я Бот-калькулятор.\n'
        'Выбери, с какими числами будешь работать.\n'
        'Для выход из калькулятора введите /cancel  ',
        reply_markup=markup_key,)
    return NUMBER

def number(update, _):
    
    user = update.message.from_user
    
    logger.info("%s выбрал %s", user.first_name, update.message.text)
    log.log_data(f"{user.first_name} выбрал {update.message.text}")
                                            
    text=  update.message.text
    if text == 'Рациональные':
        update.message.reply_text(
            'Вы выбрали рациональные числа. \n' 
            'Введите математическое выражение в виде: -3+5*(2+3^2)-5.\n'
            'Можно использовать операторы "+","-","*","/","^".\n'
            'Для завершения введите /cancel',

            reply_markup=ReplyKeyboardRemove(), # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
        )
        return RATI
    else:
        update.message.reply_text(
            'Вы выбрали комплексные числа. \n' 
            'Введите математическое выражение в виде: (5+2i)+(3+4i)\n'
            'Можно использовать операторы "+","-","*","/".\n'
            'Для завершения введи /cancel',

            reply_markup=ReplyKeyboardRemove(),
        )
        return COMP

def rac(update, _):
    user = update.message.from_user
     
    math_f = update.message.text
    
    logger.info("%s ввёл: %s", user.first_name, update.message.text)
    log.log_data(f"{user.first_name} ввёл: {update.message.text}")
    
    bool_error, text_error , number = rm.math_rational_namber(math_f)

    if bool_error == False:
        logger.info("Решение: %s = %s", update.message.text, number)
        log.log_data(f"Решение: {update.message.text} = {number}")

        update.message.reply_text(
            f'Решение: {math_f}={number}')
        
    else:
        logger.info("Ошибка: %s ", text_error)
        log.log_data(f"Ошибка: {text_error} ")
        update.message.reply_text(text_error)
 
    repeat_or_end_calc_menu(update)

    return REPEAT_OR_END_CALC
    

def komp(update, _):

    user = update.message.from_user
    math_f = update.message.text
    
    
    logger.info("Пользователь %s ввёл: %s", user.first_name, update.message.text)
    log.log_data(f"{user.first_name} ввёл: {update.message.text}")
    
    
    bool_error, text_error , number = cm.math_compleks_namber(math_f)

    if bool_error==False:

        logger.info("Решение: %s = %s", update.message.text, number)
        log.log_data(f"Решение: {update.message.text} = {number}")

        update.message.reply_text(
            f'Решение: {math_f}={number}')
        
    else:
        logger.info("Ошибка: %s ", text_error)
        update.message.reply_text(text_error) 
        log.log_data(f"Ошибка: {text_error} ")    
   
    repeat_or_end_calc_menu(update)

    return REPEAT_OR_END_CALC
    




def cancel(update, _): # Обрабатываем команду /cancel если пользователь отменил разговор
    
    user = update.message.from_user
   
    logger.info("%s вышел из калькулятора.", user.first_name)
    log.log_data(f"{user.first_name} вышел из калькулятора." )
    
    update.message.reply_text(
        'Вы вышли из калькулятора.\n'
        f'До скорых встреч {user.first_name}! ', 
        reply_markup=ReplyKeyboardRemove()
    )
   
    return ConversationHandler.END


def repeat_or_end_calc(update, context):
    user = update.message.from_user
    repeat_or_end = update.message.text
    
    if repeat_or_end=='Продолжить':

        logger.info("%s решил продолжить работу калькулятора",user.first_name)
        log.log_data(f"{user.first_name} решил продолжить работу калькулятора")

        update.message.reply_text(
            f'{user.first_name}, вы решили продолжить работу калькулятора.',
            reply_markup=ReplyKeyboardRemove())

        reply_keyboard = [['Рациональные', 'Комплексные']]
    
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        
        update.message.reply_text(
            'Выберите, с какими числами будете работать.'
            'Для выход из калькулятора введите /cancel  ',
            reply_markup=markup_key,)
        return NUMBER
       
    elif repeat_or_end=='Выход':
                
        logger.info("%s вышел из калькулятора.", user.first_name)
        log.log_data(f"{user.first_name} вышел из калькулятора.")
    
        update.message.reply_text(
            'Вы вышли из калькулятора.\n'
            f'До скорых встреч {user.first_name}! ', 
            reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END



def unknown (update, context):# 
    user = update.message.from_user
    text=update.message.text
    context.bot.send_message(update.effective_chat.id, f"{text} Странная команда, я такой не знаю!")
    logger.info(" %s ввёл %s. Данной команды не существует.",user.first_name,text)
    log.log_data(f"{user.first_name} ввёл {text}. Данной команды не существует.")


def give_word (update, context):
    word = update.message.text
    user = update.message.from_user
    logger.info(" %s ввёл %s.",user.first_name,word)
    log.log_data(f"{user.first_name} ввёл {word}.")
    
    context.bot.send_message(update.effective_chat.id, f"{user.first_name} я тебя не могу понять!")