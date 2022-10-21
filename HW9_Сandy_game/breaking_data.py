import Check as ch



def breaking_rational_data(math:str):

    
    math=math.replace(' ','')

    attributes=['^','*','/','+','-','(',')']

    for atrib in attributes:
        math=math.replace(atrib,f'#{atrib}#')
    
    list_number_math=math.split('#')
    list_data=[data for data in list_number_math if data!='']

    

    return list_data
    

def breaking_complex_data(math:str):

    
    math=math.replace(' ','')

    

    math=math.replace('(','#(')
    math=math.replace(')',')#')
    
    list_number_math=math.split('#')
    list_data=[data for data in list_number_math if data!='']


    for index,data in enumerate (list_data):
        if data != '*' and data != '/' and data != '+' and data != '-' and data != '(' and data != ')':
            if data.find('i')==-1:
                err='no i'
                return  ch.alarm_cneck(err)
            if data.find('(')==-1 or data.find(')')==-1:
                err='no ()'
                return  ch.alarm_cneck(err)
            data=data.replace('(','')
            data=data.replace(')','')
            data=data.replace('i','')
            data=data.replace('-','#-')
            data=data.replace('+','#+')
            list_data[index]=data.split('#')
    

    return False,'', list_data