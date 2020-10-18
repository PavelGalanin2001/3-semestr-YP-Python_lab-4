import random

class task2_task11:
    def __init__(self):
        self.task()
        print()

    def task(self):
        my_number = random.randint(1, 10)
        print("my_number = %d" % my_number)

        while 1:

            user_number = int(input("user_number := "))

            print("%d < %d?" % (user_number, my_number))

            if user_number < my_number:
                break

class task2_task21:
    def __init__(self, lst):
        self.lst = lst
        print(self.lst)

        self.task()
        print()

    def task(self):
        for i in range(len(self.lst)):
            length = len(self.lst[i])
            if 5 < length and length < 10:
                print(self.lst[i])

class task2_task31:
    def __init__(self):
        self.result = ''

        self.task()
        print(self.result)
        print()

    def task(self):
        self.result = ''
        for i in range(5):
            number = random.randint(65, 90)
            symbol = chr(number)
            self.result += symbol

    def getResult(self):
        return self.result

class task2_task41:
    def __init__(self, string):
        self.result = 0
        self.string = string

        self.task(string)
        print(self.result)
        print()

    def task(self, string):
        stringNumbers = '' # строка для цифр
        for i in range(len(string)): # цикл от 0 до размера строки
            number = ord(string[i]) # симол под индексом i из строки в число
            stringNumber = str(number) # число превратили в строку
            stringNumbers += stringNumber # складываем строки
        result = int(stringNumbers) # перевод строки в число
    
    def getResult(self):
        return self.result
