import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def pause():
    print('Press any key to continue...')
    string = input()

def menu():
    cls()
    print(
        """
1. Задание 1
2. Задание 2
3. Задание 3
4. Задание 4
6. Задание 6
0. Выход из из программы
        """
    )
    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    if case == ord('0'):
        return
    elif case == ord('1'):
        sum_menu_1()
        menu()
    elif case == ord('2'):
        sum_menu_2()
        menu()
    elif case == ord('3'):
        sum_menu_3()
        menu()
    elif case == ord('4'):
        sum_menu_4()
        menu()
    elif case == ord('6'):
        sum_menu_6()
        menu()
    else:
        menu()

def sum_menu_1():
    cls()
    print(
    """
1. 111
2. 121
3. 131
4. 141
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return
    elif case == ord('1'):
        import task_1_1_1
    elif case == ord('2'):
        import task_1_2_1
    elif case == ord('3'):
        import task_1_3_1
    elif case == ord('4'):
        import task_1_4_1
    else:
        return

    pause()

def sum_menu_2():
    cls()
    print(
    """
1. 211
2. 221
3. 231
4. 241
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return
    elif case == ord('1'):
        import task_2_1_1
    elif case == ord('2'):
        import task_2_2_1
    elif case == ord('3'):
        import task_2_3_1
    elif case == ord('4'):
        import task_2_4_1
    else:
        return

    pause()

def sum_menu_3():
    cls()
    print(
    """
1. 311
2. 321
4. 341
5. 353
6. 363
7. 373
8. 381
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return
    elif case == ord('1'):
        import task_3_1_1
    elif case == ord('2'):
        import task_3_2_1
    elif case == ord('4'):
        import task_3_4_1
    elif case == ord('5'):
        import task_3_5_3
    elif case == ord('6'):
        import task_3_6_3
    elif case == ord('7'):
        import task_3_7_3
    elif case == ord('8'):
        import task_3_8_1
    else:
        return

    pause()

def sum_menu_4():
    cls()
    print(
    """
1. 411
2. 421
3. 431
4. 44
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return
    elif case == ord('1'):
        import task_4_1_1
    elif case == ord('2'):
        import task_4_2_1
    elif case == ord('3'):
        import task_4_3_1
    elif case == ord('4'):
        import task_4_4
    else:
        return

    pause()

def sum_menu_6():
    cls()
    print(
    """
1. 61
2. 62
3. 63
4. 64
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return
    elif case == ord('1'):
        import task_6_1
    elif case == ord('2'):
        import task_6_2
    elif case == ord('3'):
        import task_6_3
    elif case == ord('4'):
        import task_6_4
    else:
        return

    pause()

menu()