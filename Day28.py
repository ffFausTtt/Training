# Исключения 
try:
    print(5/0)
except ZeroDivisionError: # Обработка деления на 0
    print("You can't divide by zero")

while True:
    first_number = input("First number: ")
    if first_number == 'not':
        break
    second_number = input("Second number: ")
    if second_number == 'not':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
         print("You can't divide by zero")
    else: # Код, который зависит от успешного выполнения блока try 
        print(answer)


from pathlib import Path
path = Path('alice.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print("Sorry, file not found")
else: print(contents)