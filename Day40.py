# Задачка: "Калькулятор дружбы"

def get_initials(name):
    return name[0].upper()

def calculate_friendship_index(letter1, letter2):
    return (ord(letter1.lower()) - ord('a') + 1) + (ord(letter2.lower()) - ord('a') + 1)

def main():
    first_name = input("First_name: ")
    second_name = input("Second_name: ")

    first = get_initials(first_name)
    second = get_initials(second_name)

    print(f"Первая буква: {first}")
    print(f"Вторая буква: {second}")

    index = calculate_friendship_index(first, second)
    print(f"Индекс дружбы: {index}")

if __name__ == '__main__':
    main()