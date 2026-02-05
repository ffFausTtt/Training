cars = ['audi', 'bmw', 'tyota', 'susuki']
for car in cars: 
    print(car)

for value in range(1, 5): # Результат: 1 2 3 4 (5 - не входит)
    print(value)

for value in range(6): # Результат от 0 до 5
    print(value)

numbers = list(range(1, 6)) # Формирование числового списка
print(numbers)

numbers = list(range(1, 11, 2)) # 3 аргумент - шаг 
print(numbers)

qwerty = []
for value in range(1, 11):
    num = value ** 2
    numbers.append(num)

print(numbers)
# Статистика:
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#Генератор списка:
spisok = [value ** 2 for value in range(1, 11)]
print(spisok)