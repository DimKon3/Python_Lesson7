m = int(input("Введите грузоподъемность лодки: "))
n = int(input("Введите количество рыбаков "))
count = 0

ves = sorted([int(input(f"Введите вес {_+1} рыбака ")) for _ in range(n)], reverse = True)

while len(ves):
    count += 1
    k = m - ves.pop(0)
    for i in range(len(ves)):
        if ves[i] <= k:
            ves.pop(i)
        break

print(f"Количество лодок необходимое для перевозки {count}")