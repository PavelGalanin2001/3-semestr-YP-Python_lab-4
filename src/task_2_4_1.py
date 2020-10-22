def task241(string):
    strWithNum = ''
    for i in range(len(string)):
        number = ord(string[i])
        temp = str(number)
        strWithNum += temp
    return strWithNum

def task241_main():
    print(
        """
Задание 2 "Строки и списки"

4. Пусть дана строка:

Вариант 1. На основе данной строки сформируйте новую, содержащую только цифры. Выведите новую строку.
        """
    )

    print(task241('qwerty'))

# task241_main()