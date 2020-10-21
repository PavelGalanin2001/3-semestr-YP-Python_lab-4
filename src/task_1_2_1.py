def task121(lst):
    for i in range(len(lst)):
        if (i + 1) % 2 == 0:
            print(lst[i])
            
lst = ['33', 2, 4, 5.3, 2.4, 5555.3, '443', 'ergr', 'wee', 'efe']

task121(lst)