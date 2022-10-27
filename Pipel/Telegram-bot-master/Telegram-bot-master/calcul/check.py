
def user_mode(rez: str) -> bool:
    return rez == '1' or rez == '2' or rez == '3'

'''проверка пользователя на ввод в меню'''

def user_mode2(rez: str) -> bool:
    return rez == '1' or rez == '2'

'''проверка пользователя на ввод в меню'''

# def check_realnumber():
    

def empty_line(rez: str) -> bool:
    s = len(rez)
    return s == 0

'''проверка ввода пустой строки'''

def is_compl(num):
    if " " in num:
        num1, num2 = num.split()
        result = num1.isdigit() and num2.isdigit()
        return result
    else: return False
    
'''проверка и разбитие строки на 2 значения'''

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

'''проверяет число на float'''

def is_action(x):
    return x in ["+", "-", "*", "/"]











