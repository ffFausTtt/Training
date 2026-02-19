# Передача произвольного набора аргументов
def sport(*args):
    print(args)

sport("Football")
sport("Basketball", "Sweeming", "Streetball")

# Позиционные аргументы с произвольными наборами аргументов 
def pizza(size, *toppings): # Произвольный набор указывается в конце
    print(f"Size: {size}")
    if toppings:
        for topping in toppings:
            print(topping)

pizza(24)
pizza(38, "tomatos", "chily")

# Использование произвольного набора именованных аргументов
def user(first, last, **user_info): # ** - Создание пустого словаря
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = user('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)