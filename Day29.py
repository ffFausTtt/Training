from pathlib import Path
path = Path('alice.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    pass # Ошибка без уведомления пользователя
else: print(contents)



# Хз почему, но цикл не останавливается. Он вообще не заходит в блок if
while True:
    number1 = input("First: ")
    print(repr(number1))
    number2 = input("Second: ")
    if number1 == 'not' or number2 == 'not':
        break
    try:
        sum = int(number1) + int(number2)
        print(sum)
    except ValueError:
        print("sorry")    