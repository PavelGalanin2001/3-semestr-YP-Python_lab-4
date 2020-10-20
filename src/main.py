from modules.task1 import task1_task11
from modules.task1 import task1_task21
from modules.task1 import task1_task31
from modules.task1 import task1_task41

from modules.task2 import task2_task11
from modules.task2 import task2_task21
from modules.task2 import task2_task31
from modules.task2 import task2_task41

from modules.task3 import task3_task11
from modules.task3 import task3_task21
from modules.task3 import task3_task41
from modules.task3 import task3_task53
from modules.task3 import task3_task63
from modules.task3 import task3_task73

def print_line():
    print("= = = = = - - - - - = = = = = - - - - - = = = = =")

# print("Task 1: 1.1")
# print_line()
# obj = task1_task11(1,1,1,1)
# obj = task1_task11(0,1,1,1)
# obj = task1_task11(1,0,1,1)

# print("Task 1: 2.1")
# print_line()
# obj = task1_task21([-5, 6, -11, 3, '343', 10])

# print("Task 1: 3.1")
# print_line()
# obj = task1_task31([-5, 12.24, -11.4, 6, 30, 11.98, 10])

# print("Task 1: 4.1")
# print_line()
# obj = task1_task41([-5, 12.24, -11.4, 6, 30, 11.98, 10])

# print("Task 2: 1.1")
# print_line()
# obj = task2_task11()

# print("Task 2: 2.1")
# print_line()
# obj = task2_task21(['aaaa', 'bbbbb', 'cccccc', 'ddd', 'eeeeeee', 'ff', 'gggggggggggg', 'hhhhhhhhhh'])

# print("Task 2: 3.1")
# print_line()
# obj = task2_task31()
# string = task2_task31.getResult(obj)

# print("Task 2: 4.1")
# print_line()
# obj = task2_task41(string)
# number = task2_task41.getResult(obj)

arr = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2]
]

print("Task 3: 1.1")
print_line()
obj = task3_task11(arr)

print("Task 3: 2.1")
print_line()
obj = task3_task21(arr)

print("Task 3: 4.1")
print_line()
obj = task3_task41(arr)

print("Task 3: 5.3")
print_line()
obj = task3_task53([[1,2,3,4,5], [5,4,3,2,1], [3,4,5,5,2]])

print("Task 3: 6.3")
print_line()
obj = task3_task63(arr)

print("Task 3: 7.3")
print_line()
obj = task3_task73(arr)