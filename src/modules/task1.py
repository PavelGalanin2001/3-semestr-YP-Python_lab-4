class task1_task11:
    def __init__(self, a, b, c, k):
        self.a = a
        print("a = ", end = '')
        print(self.a)

        self.b = b
        print("b = ", end = '')
        print(self.b)

        self.c = c
        print("c = ", end = '')
        print(self.c)

        self.k = k
        print("k = ", end = '')
        print(self.k)

        self.task()

        print()

    def myAbs(self, a):
        if a >= 0:
            return a
        else:
            return -a
    
    def printDelOnZero(self, var):
        print("Division by zero: %s = 0" % var)
        print("result: 00 (infinity)")

    def task(self):
        if self.a == 0:
            self.printDelOnZero('a')
        elif self.b == 0:
            self.printDelOnZero('b')
        else:
            part1 = (self.a*self.a / (self.b*self.b) + self.c*self.c*self.a*self.a)
            part2 = self.a + self.b + self.c * (self.k - self.a / (self.b*self.b*self.b))
            part3 = (self.k/self.b - self.k/self.a) * self.c
            result = self.myAbs(part1 / part2 + self.c + part3)
            print("result = ", end = '')
            print(result)

class task1_task21:
    def __init__(self, lst):
        self.lst = lst
        print(self.lst)
        self.task()
        print()
    
    def task(self):
        for i in range(len(self.lst)):
            if not isinstance(self.lst[i], str):
                if self.lst[i] > 0:
                    print(self.lst[i])
                
class task1_task31:
    def __init__(self, lst):
        self.lst = lst
        print(self.lst)
        self.task()
        print()
    
    def task(self):
        sum = 0
        for i in range(len(self.lst)):
            if self.lst[i] > 10:
                sum += self.lst[i]
        print("sum (element > 10) = ", end = '')
        print(sum)

class task1_task41:
    def __init__(self, lst):
        self.lst = lst
        print(self.lst)
        self.task()
        print()
    
    def task(self):
        max = self.lst[0]
        for i in range(len(self.lst)):
            if self.lst[i] > max:
                max = self.lst[i]
        print("max_element = ", end = '')
        print(max)