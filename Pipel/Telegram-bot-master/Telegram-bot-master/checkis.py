

def action(number, zn, number2):
    '''
    Метод выполнит математические действия
    '''
    if "." in number:
        number = float(number)
    else:
        number = int(number)
    if "." in number2:
        number2 = float(number2)
    else:
        number2 = int(number2)
    
    if zn == "+":
        number += number2
    if zn == "-":
        number -= number2
    if zn == "*":
        number *= number2
    if zn == "/":
        number /= number2
    return str(number)

def del_list(del_listi, indexi, cout):
    '''
    Метод удалит из списка все, что укажут
    '''
    i = indexi
    while i < cout + indexi:
        del_listi.pop(indexi)
        i += 1
    pass

def assembly_minus_number(listi:list) -> list:
    '''
    Метод найдет отрицательные числа в списке и отфарматирует список так,
    чтобы отрицательные числа были под одним индексом
    '''
    i = 0
    while i < len(listi):
        if listi[i] == "*" or listi[i] == "/" or listi[i] == "+" or listi[i] == "-":
            if listi[0] == "-":
                x = listi[1]
                for w in x:
                    if "." in x:
                        x = float(w) * -1
                    else:
                        x = int(w) * -1
                del_list(listi, 0, 2)
                listi.insert(0, str(x))
            if listi[i] == "-" and listi[i - 1] in ["-", "+", "*", "/", "("] and i != 0:
                x = listi[i + 1]
                for w in x:
                    if "." in x:
                        x = float(w) * -1
                    else:
                        x = int(w) * -1
                del_list(listi, i, 2)
                listi.insert(i, str(x))
        i += 1
    return listi

def calculation(stroka) -> str:
    '''
    Метод примет список примера, отфарматированного assembly_minus_number
    и выдаст ответ
    '''
    l = 0
    while l < len(stroka):
        if stroka[l] == "*" or stroka[l] == "/":
            x = action(stroka[l - 1], stroka[l], stroka[l + 1])
            del_list(stroka, l - 1, 3)
            stroka.insert(l - 1, x)
            l -= 1
        l += 1
    k = 0
    while k < len(stroka):
        if stroka[k] == "+" or stroka[k] == "-":
            x = action(stroka[k - 1], stroka[k], stroka[k + 1])
            del_list(stroka, k - 1, 3)
            stroka.insert(0, x)
            k -= 1
        k += 1
    result = ""
    for i in stroka:
        result += str(i)
    return result

def queue(stroka):
    '''
    Метод определит очередность выполнения примера и тут же выполнит его
    '''
    x = 0
    while True:
        if "(" in stroka:
            index_max_skob_open = 0
            index_min_skob_closed = len(stroka)
            i = 0
            while i < len(stroka):
                if stroka[i] == "(" and i > index_max_skob_open:
                    index_max_skob_open = i
                i += 1
            a = 0
            while a < len(stroka):
                if stroka[a] == ")"and a > index_max_skob_open:
                    index_min_skob_closed = a
                    break
                a += 1
                    
            list_cont = []
            j = index_max_skob_open + 1
            while j < index_min_skob_closed:
                list_cont.append(stroka[j])
                j += 1
            y = len(list_cont)

            x = calculation(list_cont)
            del_list(stroka, index_max_skob_open, y + 2)
            stroka.insert(index_max_skob_open, x)
        else:
            break
    if len(stroka) > 1:
        x = calculation(stroka)
        if "." in x:
            result = x
        else:
            result = x
        return result
    else:
        result = 0
        for i in stroka:
            if "." in i:
                result = i
            else:
                result = i
            return result

def assembly_example(stroka:str) -> str:
    '''
    Метод соберет математическон выражение, если оно есть в
    аргументе, при этом отбросив мусор, проверит достаточно ли числовых данных,
    проверит на правильность ввода и корректность записи скобок, выведет результат
    '''
    result = ""
    i = 0
    while i < len(stroka):
        if stroka[i] in ["+", "-", "*", "/", "(", ")"]:
            result += stroka[i] + " "
        if stroka[i].isdigit() or stroka[i] in ["."]:
            if i != len(stroka) - 1:
                if stroka[i + 1].isdigit() or stroka[i] in ["."] or stroka[i + 1] == ".":
                    result += stroka[i]
                else:
                    result += stroka[i] + " "
            else:
                result += stroka[i]
        i += 1

    result = result.split( )

    number = 0
    skobki_open = 0
    skobki_closed = 0
    snaki = 0
    for i in result:
        z = str(i)
        for j in z:
            if j.isdigit():
                number += 1
                break
        if i == "(":
            skobki_open += 1
        if i == ")":
            skobki_closed += 1
        
    assembly_minus_number(result)
    for i in result:
        if i == "+" or i == "-" or i == "*" or i == "/":
            snaki += 1

    if number != snaki + 1:
       # print("Недостаточно числовых данных!")
        return "Недостаточно числовых данных!"
    if number == 0:
      #  print("Неправильный ввод: нужны числа!")
        return "Неправильный ввод: нужны числа!"
    if skobki_open != skobki_closed:
      #  print("Некорректная запись скобок!")
        return "Некорректная запись скобок!"

    return queue(result)
