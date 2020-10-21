def task131(lst):
    sum = 0
    for i in range(len(lst)):
        if lst[i] > 10:
            sum += lst[i]
    print(sum)
    
lst = [-10, 5, 6, 15, 3, 16, 7]

task131(lst)