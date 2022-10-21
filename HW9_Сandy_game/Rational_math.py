from cgitb import text
import breaking_data as bd
import Check as ch


def math_rational_namber(data:str):
    
    
    def math_operations(list_data):
        try:
            if list_data[0]=='-':
                list_data[1] = str(float(list_data[1])*(-1))
                list_data.pop(0)

            elif  list_data[0]=='+':
                list_data.pop(0)
        except (ZeroDivisionError,ValueError,IndexError) as err:
                return ch.alarm_cneck(str(err))

        while True:
            try:
                float(list_data[0])
                if list_data.count('^')>0:
                    attr='^'
                elif list_data.count('*')>0 or list_data.count('/')>0:
                    if list_data.count('*')>0 and list_data.count('/')>0 and (list_data.index('*')<list_data.index('/')):
                        attr='*'
                    elif list_data.count('*')>0 and list_data.count('/')>0 and (list_data.index('/')<list_data.index('+')):
                        attr='/'
                    elif list_data.count('*')>0:
                        attr='*'
                    else:
                        attr='/'
                elif list_data.count('+')>0 or list_data.count('-')>0:
                    if list_data.count('+')>0 and list_data.count('-')>0 and (list_data.index('+')<list_data.index('-')):
                        attr='+'
                    elif list_data.count('-')>0 and list_data.count('+')>0 and (list_data.index('-')<list_data.index('+')):
                        attr='-'
                    elif list_data.count('+')>0:
                        attr='+'
                    else:
                        attr='-'
                else:
                    break
            
                index_attribute = list_data.index(attr)
                if attr=='^':
                    temp_number=float(list_data[index_attribute-1])**float(list_data[index_attribute+1])
                elif attr=='*':
                    temp_number=float(list_data[index_attribute-1])*float(list_data[index_attribute+1])
                elif attr=='/':
                    temp_number=float(list_data[index_attribute-1])/float(list_data[index_attribute+1])
                elif attr=='+':
                    temp_number=float(list_data[index_attribute-1])+float(list_data[index_attribute+1])
                elif attr=='-':
                    temp_number=float(list_data[index_attribute-1])-float(list_data[index_attribute+1])
                temp_number=str(temp_number)
            except (ZeroDivisionError,ValueError,IndexError) as err:
                return ch.alarm_cneck(str(err))

            for i in range(3):
                list_data.pop(index_attribute-1)

            list_data.insert(index_attribute-1,temp_number)
        
        number_maths = list_data[0]
        tex_error = ''
        bool_error = False
        return bool_error,tex_error, number_maths


    def quotes_math(list_number_attributes:list):

        while list_number_attributes.count('(')>0:
            try:
                index_el_1=-1
                index_el_2=-1

                for i,x in enumerate (list_number_attributes):
                    if x=='(':
                        index_el_1=i
                    if x==')' and index_el_1!=-1:
                        index_el_2=i
                        break

                new_list_number=[]

                new_list_number=[list_number_attributes[ind] for ind in range(index_el_1+1,index_el_2)]

                bool_error, text_error, temp_number = math_operations(new_list_number)
                if bool_error==True:
                    return bool_error, text_error, temp_number

                for de in range(index_el_2-index_el_1+1):
                    list_number_attributes.pop(index_el_1)

                list_number_attributes.insert(index_el_1,str(temp_number))

                new_list_number.clear()
            except (ZeroDivisionError,ValueError,IndexError) as err:
                return ch.alarm_cneck(str(err))

        bool_error, text_error ,number= math_operations (list_number_attributes)
        
        return bool_error, text_error ,number
    
    
    list_data_number=bd.breaking_rational_data(data)

    bool_error, text_error , number=quotes_math(list_data_number)


    return bool_error, text_error , number
