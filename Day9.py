cars = ['audi', 'bmw', 'toyota', 'honda', 'subaru']

for car in cars:
    if car == 'bmv':
        print(car.upper())
    else: print(car.title())

car = 'Audi'
# car != 'audi' регистр важен! 
if car.lower() == 'audi':
    print(car)

# Составные условия: and, or
age_1 = 18
age_2 = 15

if age_1 >= 18 and age_2 >= 18: # Оба должны быть истиными
    print("Пиво может купить каждый")

if age_1 >= 18 or age_2 >= 18: # Хотя бы одно должно быть истинным
    print("Пиво может купить только 1 из них")


# Проверка вхождения значения в список
if 'toyota' in cars:
    print('toyota in cars')
#Проверка отсутствия значения в списке
if 'cherry' not in cars:
    print("cherry not in cars")

# В операторе if можно использовать любые математические сравнения: <, <=, >, >=, ==, !=

if cars: # Проверка наличия содержимого в списке. Возвращает True, если список содержит хотя бы 1 элемент
    print(cars)

age_3 = int(input("Введите Ваш возраст: "))
if age_3 <= 0:
    print("Возраст не коректный")
elif age_3 >= 18:
    print("Вы взрослый")
elif age_3 < 18:
    print("Вы ребенок")
# Блок Else не обязателен