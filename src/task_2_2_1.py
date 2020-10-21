def task221(lst):
    for i in range(len(lst)):
        length = len(lst[i])
        if 5 < length and length < 10:
            print(lst[i])
            
lst = [
    'aaa',
    'bbbbbb',
    'ccccc',
    'dddddddddd',
    'eeeeeeeee'
]

task221(lst)