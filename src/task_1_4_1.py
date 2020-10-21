def task141(lst):
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    print(max)
    
lst = [4, 7, 2, -100, 3, 55, 33, 6]

task141(lst)