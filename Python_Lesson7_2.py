import random

count = int(input("Введите сколько чисел будет в массиве: "))
a = [random.randint(1,10000) for _ in range(count)]
print(a)
a.insert(0,a[-1])
del a[-1:]
print(a)