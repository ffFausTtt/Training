alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'yellow', 'points': 10}
alien_3 = {'color': 'red', 'points': 15}

# Список словарей
aliens = [alien_1, alien_2, alien_3] 
for alien in aliens: 
    print(alien)

aliens = []
# Создание 30 экземпляров 
for number in range(30):
    new_alien = {'color': 'green', 'points': 5}
    aliens.append(new_alien)
print(aliens)

print(len(aliens)) # Вывод количества элементов

for alien in aliens[:5]:
    print(alien) # Вывод данных о первых 5 элементах 

# Изменение части элементов в списке словарей
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

# Список в словаре
user = {
    'name': 'Artyom', 
    'hobby': ['programming', 'guitar', 'sport', 'books']
    }
for k, v in user.items():
    print(k)
    print(v)

# Словари в словаре
users = {
    'Artyom': {
        'age': 21,
        'heir_color': 'black',
        'body': 'medium'
    },
    'Igor' : {
        'age': 21,
        'heir_color': 'blond',
        'body': 'hard'
    }
}

for name, info in users.items():
    print(name)
    print(info)