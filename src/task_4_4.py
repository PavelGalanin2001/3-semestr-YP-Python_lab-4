def task44(string):
    counter = 0
    for i in string:
        counter += 1
    print('number symbols: %d' % counter)
    
    words = string.split()
    print("number words: %d" % len(words))

string = 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты.'

print(string)
print()
task44(string)