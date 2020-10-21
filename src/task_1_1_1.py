import math

def task111(a, b, c, k):
    if a == 0:
        print("a = 0. Error: div on zero")
        return -1
    elif b == 0:
        print("b = 0. Error: div on zero")
        return -1
    else:
        part1 = math.pow(a, 2) / math.pow(b, 2) + math.pow(c, 2) * math.pow(a, 2)
        part2 = a + b + c * (k - a / math.pow(b, 3))
        part3 = c + (k/b - k/a) * c
        result = part1 + part2 + part3
        if result >= 0:
            return result
        else:
            return -result

print(task111(0,1,1,1))
print(task111(1,0,1,1))
print(task111(1,1,1,1))