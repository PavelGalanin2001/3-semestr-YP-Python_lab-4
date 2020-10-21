def task241(string):
    strWithNum = ''
    for i in range(len(string)):
        number = ord(string[i])
        temp = str(number)
        strWithNum += temp
    return strWithNum
        
print(task241('qwerty'))