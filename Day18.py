# Передача списка
def greet_users(names):
    for name in names: 
        mes = (f"Hello {name.title()}!")
        print(mes)
    names.append('Kosty') # В функциях можно изменять данные. Изменения постоянные
    return names

user_names = ['artyom', 'Igor', 'tom', 'Isaack']
us_name = greet_users(user_names)
print(us_name)

# Запрет изменения списка
copy_names = user_names[:] # Создание копии (среза)
copy = greet_users(copy_names) # Передача копии, оригинал остается нетронутым
print(copy)
print(us_name)