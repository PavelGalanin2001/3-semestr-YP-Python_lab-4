def task621(lst, addedLst):
    for i in range(len(addedLst)):
        lst.pop(0)
    for i in range(len(addedLst) - 1, -1, -1):
        lst.insert(0, addedLst[i])
    return lst
    
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst)
lst = task621(lst, [111, 222, 333])
print(lst)