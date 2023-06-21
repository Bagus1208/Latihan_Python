# def add(x, y):
#     return x + y

# def do_twice(func, x, y):
#     return func(func(x, y), func(x, y))

# a = 5
# b = 10

# print(do_twice(add, a, b))

# """
# Rumusnya

# add(add(5, 10), add(5, 10))
# add(15 , 15)
# 30 
# """

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(func(4))