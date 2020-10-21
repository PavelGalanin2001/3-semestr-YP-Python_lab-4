import random

def task231():
    result = ''
    for i in range(5):
        number = random.randint(65, 90)
        symbol = chr(number)
        result += symbol
    return result

print(task231())