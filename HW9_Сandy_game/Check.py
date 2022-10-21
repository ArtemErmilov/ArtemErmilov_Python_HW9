

def alarm_cneck (err:str):
    if err == 'float division by zero':
        return True,'При решение уравнения появилось деление на 0', None
    elif err.find('could not convert string to float:')>-1:
        return True,'Уравнение введено неправильно,вместо цифр введены буквы',None
    elif  err.find('no signs')>-1:
        return True,'Уравнение введено неправильно.Не хватает оператор математических выражений',None
    elif err.find('list index out of range')>-1:
        return True,'Уравнение введено неправильно.',None
    elif err=='no i':
        return True,'Уравнение введено неправильно.В комплексном числе не хватает i.',None
    elif err=='no ()':
        return True,'Уравнение введено неправильно.В комплексном числе не хватает скобочек.',None
    else:
        return True,'Уравнение введено неправильно.',None
    