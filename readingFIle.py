# file = open("Python/skipAngka.py", 'r')

# # cont = file.readlines()
# # print(cont)
# # file.close()

# for i in file:
#     print(i)

# file.close()

# file = open("Python/Book.txt", "r")
# for i in file:
#     if i[-1] == '/':
#         print(i[0] + str(len(i) - 1))
#     else:
#         print(i[0] + str(len(i)))
# file.close()

def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

print(pure_function(4,2))