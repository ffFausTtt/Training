import this # Дзен Python

names = ['bob', 'ryck', 'issak'] 
print(f"Hi {names[0].title()}, {names[1].title()}, {names[2].title()}")  #  Вывод элементов в списке (функции для строк - таке применимы)

names[0] = 'Igor' # Замена элемента в списке
print(names)

names.append('Allen') # Добавление элементов в конец списка
print(names)

car = [] # Можно начать с пустого списка
car.append('honda')
car.append('jetta')
car.append('suzuki')
print(car)

car.insert(1, 'lada') # Добавление элементов в произвольную позицию (все элементы сдвигаются)
print(car)

del car[2] # Оператор del удаляет элемент из конкретной позиции по его индексу
print(car)

popped_car = car.pop() # Метод pop выталкивает последний элемент из списка, удаляет его, но с ним можно продолжить работу. Можно указывать индексы для удаления конкретного элемента, например: popped_car = car.pop(1)
print(car)
print(popped_car)

car.remove('honda') # Удаление элемента по значению (ВАЖНО: удаляет только первое вхождение заданного значения)
print(car)