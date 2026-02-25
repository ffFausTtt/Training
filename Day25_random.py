from random import randint
print(randint(1,6)) # randint генерирует случайное число в дипазоне (включительно)

from random import choice
players = ['artyom', 'andy', 'igor']
first = choice(players) # choice - получает список или кортеж и возвращает случайно выбранный элемент
print(first.title())