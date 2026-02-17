def user(age, name='Bob'): # Значение по умолчанию. Должно следовать в конце параметров.
    print(f"Hello {name}, your {age} years")

user(age=15) # Именованный формат
user(20) # Позиционный формат

def format_name(first_name, second_name, last_name=''): # 3 параметр - необязательный, поэтому задаем пустое значение по умолчанию
    if last_name:
        full_name = f"{first_name} {second_name} {last_name}"
    else: full_name = f"{first_name} {second_name}"
    return full_name.title() # Возвращение значения

person = format_name('jimi', 'hendrix') # Переменной присваеваем результат выполнения функции
print(person)

last_person = format_name('andru', 'denias', 'birsac')
print(last_person)

def build_person(first_name, last_name):
    person = {
        'first' : first_name,
        'last' : last_name
    }
    return person # Возвращение словаря

build = build_person('Artyom', 'Moskalenko')
print(build)