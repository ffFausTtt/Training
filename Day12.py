user = {
    'login' : 'Artyom',
    'password' : 'Art_admin'
}
# Перебор всех пар "ключ-значение"
for key, value in user.items(): # items() - возвращает список пар "ключ-значние"
    print(f"Key: {key}")
    print(f"Value: {value}")
'''
Key: login
Value: Artyom
Key: password
Value: Art_admin
'''

# Перебор всех ключей в словаре
for sett in user.keys():
    print(sett)
'''
login
password
'''

# Перебор всех значений в словаре
for val in user.values():
    print(val)
'''
Artyom
Art_admin
'''

lengs = {
    'Artyom' : 'Python',
    'Igor' : 'PHP',
    'Bob' : 'Python'
}
# Вывод без дубликатов - set()
for leng in set(lengs.values()):
    print(leng)
'''
PHP
Python
'''