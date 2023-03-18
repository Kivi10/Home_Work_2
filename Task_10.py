import random

coinsNumber = int(input("Введите число монеток на столе -> "))
null = 0
one = 0

while coinsNumber > 0:
    i = random.randint(0, 1)
    if i == 0:
        null += 1
    if i == 1:
        one += 1
    coinsNumber -= 1
    print(i)

if one > null:
    print("Минимальное число монеток, которое нужно перевернуть =", null)
else:
    print("Минимальное число монеток, которое нужно перевернуть =", one)
