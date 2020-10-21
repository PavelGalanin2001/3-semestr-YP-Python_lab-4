def task431(string):
    arr = string.split('_')
    
    for i in range(len(arr)):
        arr[i] = arr[i].split(';')
        surname = arr[i][0]
        name = arr[i][1]
        middlename = arr[i][2]
        age = arr[i][3]
        category = arr[i][4]
        
        name_surname_middlename = name + ' ' + surname + ' ' + middlename
        
        if surname == 'Петров':
            print(surname)
            print(name)
            print(middlename)
            print(age)
            print(category)
            print()
            #print("%12s\t%12s\t%12s\t%12s\t%16s" % (surname, name, middlename, age, category))

my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'

task431(my_string)