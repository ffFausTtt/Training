dogs = {'color' : 'grey', 'age' : 5}
print(dogs['color'])
print(dogs['age'])

# Добавление пар "ключ-значение" в словарь:
dogs['weght'] = 10
print(dogs)

#Изменение пар "ключ-значение" в словаре:
dogs['age'] = 6
print(dogs)

#Удаление пар "ключ-значение" в словаре:
del dogs['weght']
print(dogs)

# Обращение к значениям методом get()
new_dogs = dogs.get("poroda", "No poroda in dogs") # 1 аргумент - что ищем, 2 аргумент - что вывести в случае неудачи. 2 аргумент - не обязаелен (вернет None)
print(new_dogs)