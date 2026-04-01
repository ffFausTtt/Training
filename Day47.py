# Задача: "Калькулятор чаевых"

while True:
    try:
        all_sum = float(input("Сумма счета: "))
        proc = float(input("Процент чаевых: "))
        count_person = int(input("Кол-во человек: "))
        
        if count_person <= 0:
            print("Количество человек должно быть положительным числом!")
            continue
            
        cash = (all_sum + (all_sum * proc / 100)) / count_person
        print(f"Каждый должен заплатить по: {cash:.2f} руб.")
        break  # Выходим из цикла, если всё прошло успешно
        
    except ValueError:
        print("Ошибка: нужно ввести число! Попробуйте снова.\n")