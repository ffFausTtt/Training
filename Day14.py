promt = 'Введите текст: '
message = '' # Объявляем заранее, чтобы были первичные данные для сравнения
while message != 'not':
    message = input(promt)
    print(message)

while message != 'not':
    message = input(promt)
    if message != 'not': # Проверка, чтобы не выводить строку-отмены
        print(message)

# Флаги
flag = True
while flag:
    message = input(promt)
    if message == 'not':
        flag = False
    else: print(message)

promt = 'City: '
while True:
    city = input(promt)
    if city == 'NN':
        break # Остановка цикла 
    else: print(city)

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue # Возвращение к началу цикла
    print(num)