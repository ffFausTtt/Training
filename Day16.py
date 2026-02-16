def hi_user(): # Определение функции
    print("Hello!")

hi_user() # Вызов функции

# Передача данных в функцию 
def greet_user(name): # name в определении функции - это параметр, значение Igor - аргумент
    print(f"Hello, {name}!")

greet_user('Igor')

# Позиционная передача данных (порядок ВАЖЕН!)
def greet_user(name, age): # Позиционные параметры - таже последовательность что и у аргументов
    print(f"Hello, {name}! Your {age} years")
# Множественный вызов функции
greet_user('Igor', 21)
greet_user('Art', 21)

# Именованная передача данных 
greet_user(age = 51, name = 'Andrey') # Связь параметров и аргументов 