import math

class task3_task11:
    def __init__(self, arr):
        self.arr = arr
        self.print_arr(arr)
        self.task()
        self.print_arr(arr)
        print()

    def task(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                self.arr[i][j] = math.pow(self.arr[i][j], 2)

    def print_arr(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print("%4d" % (arr[i][j]), end = '')
            print()
        print()

class task3_task21:
    def __init__(self, arr):
        self.arr = arr
        self.task()
        print()

    def task(self):
        for i in range(len(self.arr)):
            sum = 0
            for j in range(len(self.arr[i])):
                sum += self.arr[i][j]
                print("%4d" % (self.arr[i][j]), end = '')
            print("\t%d" % (sum))

class task3_task41:
    def __init__(self, arr):
        self.arr = arr
        self.task()
        print()

    def task(self):
        for i in range(len(self.arr)):
            mult = 1
            for j in range(len(self.arr[i])):
                mult *= self.arr[i][j]
                print("%4d" % (self.arr[i][j]), end = '')
            print("\t%d" % (mult))

class task3_task53:
    def __init__(self, arr):
        self.arr = arr
        print(self.arr)
        self.task()
        print(self.arr)
        print()

    def task(self):
        for i in range(len(self.arr)):
            mult = 1
            for j in range(len(self.arr[i])):
                if self.arr[i][j] == 5:
                    self.arr[i][j] = 25

class task3_task63:
    def __init__(self, arr):
        self.arr = arr
        print(self.arr)
        self.task()
        print(self.arr)
        print()

    def task(self):
        for i in range(len(self.arr)):
            mult = 1
            for j in range(len(self.arr[i])):
                self.arr[i][j] = 0

class task3_task73:
    def __init__(self, arr):
        self.arr = arr
        self.counter = 0
        print(self.arr)
        self.task()
        print(self.counter)
        print()

    def task(self):
        counter = 0
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                if self.arr[i][j] == 3:
                    counter += 1