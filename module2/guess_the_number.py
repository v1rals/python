#! /usr/bin/python3
import random
rnd = random.randrange(1, 100)
print("Я загадал число, может быть это", rnd ,",а может и нет")
while True:
    guess = int(input('Попробуй угадать число: '))
    if guess > rnd:
        print("Переборщил")
        continue
    if guess < rnd:
        print("Недоборщил")
        continue
    else:
        print("В самую точку!")
        break
