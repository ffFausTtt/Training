# Хранение функций в модулях 
def user(first_name, last_name, *info):
    full_name = f"{first_name} {last_name}"
    print(f"Hello {full_name.title()}")
    for date in info:
        print(f"Info: {date}")