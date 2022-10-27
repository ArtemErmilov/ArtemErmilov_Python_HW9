from asyncore import dispatcher
from turtle import update
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
from checkis import assembly_example
from calcul import loger, complex_number, check
# import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
from random import randint

bot = Bot(token = TOKEN)
updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

CHOICE, RAZION, COMPLEX, OPERATION = range(4)

def start(update, context):   # это эхо-бот
    text = context.args
    if not text:
        context.bot.send_message(update.effective_chat.id, "Привет!")
    else:
        texti = ""
        for i in text:
            texti += i
        context.bot.send_message(update.effective_chat.id, texti)

def calculator(update, _):
    reply_keyboard = [['1', '2']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)  # /calculator
    update.message.reply_text(
        "Приветствуем вас в нашем калькуляторе!\n"
        "Вы будете работать с комплексными или рациональными числами?\n\n"
        "Введите 1 если с рациональными или 2 если с комплексными",
        reply_markup=markup_key,)
    return CHOICE

def choice(update, _):
    choic = update.message.text
    if choic == "1":
        loger.dif_log(f'Выбраны рациональные числа')
        update.message.reply_text("Введите выражение вида- 1+(1*1+1/1(1/1+1-1*1)+1-1/1*1)*1")  #, reply_markup=ReplyKeyboardRemove())
        return RAZION
    if choic == "2":
        loger.dif_log(f'Выбраны комплексные числа')
        update.message.reply_text('Введите первое комплексное число (действительная и мнимая части разделяются пробелом)')
        return COMPLEX

def razional(update, _):
    num = update.message.text
    loger.dif_log(f'Введено выражение: {num}')
    result = assembly_example(num)
    loger.dif_log(f'Результат выражения: {result}')
    update.message.reply_text(result)
    return ConversationHandler.END

num1 = ""
num2 = ""
def komplex(update, _):   # , reply_markup=ReplyKeyboardRemove()
    global num1
    global num2
    if num1 == "":
        num1 = update.message.text
        loger.dif_log(f'Введено комплексное число: {num1}')
        if not check.is_compl(num1):
            update.message.reply_text(f'Неверный ввод: {num1}')
            update.message.reply_text('Введите первое комплексное число (действительная и мнимая части разделяются пробелом)')
            num1 = ""
        else: update.message.reply_text('Введите второе комплексное число (действительная и мнимая части разделяются пробелом)')
        return COMPLEX
    else:
        num2 = update.message.text
        if not check.is_compl(num2):
            update.message.reply_text(f'Неверный ввод: {num2}')
            num2 = ""
            update.message.reply_text('Введите второе комплексное число (действительная и мнимая части разделяются пробелом)')
            return COMPLEX
        loger.dif_log(f'Введено комплексное число: {num2}')
    if num2 != "":
        update.message.reply_text('Что Вы хотите сделать с этими числами? (+,-,*,/)')
        return OPERATION

def operation(update, _):
    global num1
    global num2
    rez = 0
    znak = update.message.text
    if not check.is_action(znak):
        loger.dif_log(f'Неверный ввод: {znak}')
        update.message.reply_text('Что Вы хотите сделать с этими числами? (+,-,*,/)')
        return OPERATION
    loger.dif_log(f'Введено действие с числами: {znak}')
    num1_tuple = (float(num1.split()[0]), float(num1.split()[1]))
    num2_tuple = (float(num2.split()[0]), float(num2.split()[1]))
    update.message.reply_text(num1_tuple)
    update.message.reply_text(num2_tuple)
    if znak == '+':
        rez = complex_number.sum_compl(num1_tuple, num2_tuple)

    elif znak == '-':
        rez = complex_number.sub_compl(num1_tuple, num2_tuple)

    elif znak == '*':
        rez = complex_number.mult_compl(num1_tuple, num2_tuple)

    elif znak == '/':
        rez = complex_number.div_compl(num1_tuple, num2_tuple)
    update.message.reply_text(rez)
    loger.dif_log(f'Результат: {rez}')
    num1 = ""
    num2 = ""
    return ConversationHandler.END

# RULES
CHOICE, TAKE_I, TAKE_BOT = range(3)

def game(update, _):
    reply_keyboard = [['орел', 'решка']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)  # /calculator
    update.message.reply_text("Приветствуем вас в нашей игре!")
    update.message.reply_text("Выберите, орел или решка?", reply_markup=markup_key,)
    return CHOICE

#boo = True
konfet = 202
def choice_game(update, _):
    choic = update.message.text
  #  global boo 
    choice = randint(0, 1)
    if choice == 0:
        update.message.reply_text("Выпал орел!")
        choice = "орел"
    if choice == 1:
        update.message.reply_text("Выпала решка!")
        choice = "решка"
    if choic.lower() == choice:
        update.message.reply_text("Вы выиграли, ваш ход первый!")
        loger.dif_log(f'Пользователь победил и ходит первый!')
        update.message.reply_text("Забрать за один ход можно не больше 28 конфет, тот, кто берет последнюю конфету - проиграл.")
        update.message.reply_text(f"На столе {konfet} конфет.")
        update.message.reply_text("Сколько берете конфет, хозяин?!")
 #       boo = True
        return TAKE_I
    else:
        update.message.reply_text("Вы проиграли, ходит первым бот!")
        loger.dif_log(f'Пользователь проиграл и ходит первым бот!')
        update.message.reply_text("Забрать за один ход можно не больше 28 конфет, тот, кто берет последнюю конфету - проиграл.")
        update.message.reply_text(f"На столе {konfet} конфет.")
 #       boo = False
        return TAKE_BOT

# def rules(update, _):
#     global boo 
#     global konfet
#     print(boo)
#     print(konfet)
#     update.message.reply_text("Забрать за один ход можно не больше 28 конфет, тот, кто берет последнюю конфету - проиграл.")
#     update.message.reply_text(f"На столе {konfet} конфет.")
#     if boo:
#         update.message.reply_text("Сколько берете конфет, хозяин?!")
#         return TAKE_I
#     else:
#         return TAKE_BOT

def take_i(update, _):
    global konfet
    if konfet > 0:
        number = update.message.text
        if number.isdigit():
            if int(number) > 0 and int(number) < 29 and int(number) <= konfet:
                konfet -= int(number)
                update.message.reply_text(f"На столе осталось {konfet} конфет.")
                loger.dif_log(f'Пользователь забирает {number} конфет, осталось {konfet}')
                return TAKE_BOT
            else: 
                update.message.reply_text("Можно брать не больше 28 конфет, не меньше одной \
                и не больше общего количества конфет!")
                update.message.reply_text("Сколько берете конфет?")
                loger.dif_log(f'Пользователь ввел {number}, это неверный ввод')
                return TAKE_I
        else: 
            update.message.reply_text("Неверный ввод.")
            update.message.reply_text("Можно брать не больше 28 конфет и не меньше одной!")
            update.message.reply_text("Сколько берете конфет?")
            loger.dif_log(f'Пользователь ввел {number}, это неверный ввод')
            return TAKE_I
    else:
        update.message.reply_text("Вы победили, о Великий!!!")
        loger.dif_log('Пользователь победил!')
        return ConversationHandler.END

def take_bot(update, _):
    global konfet
    if konfet > 0:
        if konfet != 1:
            if konfet > 48:
                take = randint(1, 28)
                konfet -= take
                update.message.reply_text(f"Бот забирает {take} конфет")
                update.message.reply_text(f"На столе осталось {konfet} конфет.")
                update.message.reply_text("Сколько берете конфет, хозяин?!")
                loger.dif_log(f'Бот забирает {take} конфет, осталось {konfet}')
                return TAKE_I
            if konfet <= 48 and konfet > 29:
                take = konfet - 30
                konfet -= take
                update.message.reply_text(f"Бот забирает {take} конфет")
                update.message.reply_text(f"На столе осталось {konfet} конфет.")
                update.message.reply_text("Сколько берете конфет, хозяин?!")
                loger.dif_log(f'Бот забирает {take} конфет, осталось {konfet}')
                return TAKE_I
            if konfet <= 29:
                take = konfet - 1
                konfet -= take
                update.message.reply_text(f"Бот забирает {take} конфет")
                update.message.reply_text(f"На столе осталось {konfet} конфет.")
                update.message.reply_text("Сколько берете конфет, хозяин?!")
                loger.dif_log(f'Бот забирает {take} конфет, осталось {konfet}')
                return TAKE_I
        else:
            konfet -= 1
            update.message.reply_text("Бот забирает 1 конфету")
            update.message.reply_text("На столе осталось 0 конфет.")
            loger.dif_log('Бот забирает 1 конфету, осталось 0')
            return TAKE_I
    else:
        update.message.reply_text("Бот победил Вас, о Великий!!!")
        loger.dif_log('Бот победил!')
        return ConversationHandler.END

def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    loger.dif_log("Пользователь выключил калькулятор.")
    # Отвечаем на отказ поговорить
    update.message.reply_text('Bai!',reply_markup=ReplyKeyboardRemove())
    # Заканчиваем разговор.
    return ConversationHandler.END

conv_handler = ConversationHandler(entry_points=[CommandHandler('calculator', calculator)],
    states={
        CHOICE: [MessageHandler(Filters.regex('^(1|2)$'), choice)],
        RAZION: [MessageHandler(Filters.text & ~Filters.command, razional)],
        COMPLEX: [MessageHandler(Filters.text & ~Filters.command, komplex)],
        OPERATION: [MessageHandler(Filters.text & ~Filters.command, operation)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

conv_handler2 = ConversationHandler(entry_points=[CommandHandler('game', game)],
    states={
        CHOICE: [MessageHandler(Filters.regex('^(орел|решка)$'), choice_game)], # RULES: [MessageHandler(Filters.text & ~Filters.command, rules)],
        TAKE_I: [MessageHandler(Filters.text & ~Filters.command, take_i)],
        TAKE_BOT: [MessageHandler(Filters.text & ~Filters.command, take_bot)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

  

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(conv_handler2)

dispatcher.add_handler(CommandHandler("start", start))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, calculator))

print("Сервер запущен!")
updater.start_polling() 
updater.idle()