from modules.task1 import task1_task11
from modules.task1 import task1_task21
from modules.task1 import task1_task31
from modules.task1 import task1_task41

from modules.task2 import task2_task11
from modules.task2 import task2_task21
from modules.task2 import task2_task31
from modules.task2 import task2_task41

def print_line():
    print("= = = = = - - - - - = = = = = - - - - - = = = = =")

print("Task 1: 1.1")
print_line()
obj = task1_task11(1,1,1,1)
obj = task1_task11(0,1,1,1)
obj = task1_task11(1,0,1,1)

print("Task 1: 2.1")
print_line()
obj = task1_task21([-5, 6, -11, 3, '343', 10])

print("Task 1: 3.1")
print_line()
obj = task1_task31([-5, 12.24, -11.4, 6, 30, 11.98, 10])

print("Task 1: 4.1")
print_line()
obj = task1_task41([-5, 12.24, -11.4, 6, 30, 11.98, 10])

print("Task 2: 1.1")
print_line()
obj = task2_task11()

print("Task 2: 2.1")
print_line()
obj = task2_task21(['aaaa', 'bbbbb', 'cccccc', 'ddd', 'eeeeeee', 'ff', 'gggggggggggg', 'hhhhhhhhhh'])

print("Task 2: 3.1")
print_line()
obj = task2_task31()
string = task2_task31.getResult(obj)

print("Task 2: 4.1")
print_line()
obj = task2_task41(string)
number = task2_task41.getResult(obj)
