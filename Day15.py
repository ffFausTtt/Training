unconfirmed_users = ['alice', 'brian', 'bob']
confirmed_users = []
# Перемещение элементов между списками 
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Проверенный пользователь: {current_user.title()}")
    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['cat', 'dog', 'cat', 'dog']
print(pets)
#Удаление всех вхождений из списка
while 'cat' in pets: 
    pets.remove('cat')
print(pets)

# Заполнение словаря данными? введенными пользователем
responses = {}
active = True
while active:
    name = input("Name: ")
    response = input("Response: ")

    responses[name] = response
    last = input("Last? ")
    if last == 'no':
        active = False

for name, response in responses.items():
    print(f"{name} - {response}")