import random

count = int(input("Введите сколько чисел будет в массиве: "))
a = [random.randint(1,10000) for _ in range(count)]
print(a)

# 3 вариант
b = a[::-1]
print(b)

# 2 вариант
b = list(reversed(a))
print(b)

# 1 вариант
b = a
b.reverse()
print(b)