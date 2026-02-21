class Dog: # Классы называются с заглавной буквы
    def __init__(self, name, age): # Метод __init__ - специальный метод? который выполняется автоматически при создании каждого нового экземпляра
               # self - ссылка на экземпляр (обязательный параметр), предоставляет доступ к атребутам и методам класса
        self.name = name # Переменные с префиксом self досупны для любого метода в классе
        self.age = age # Берет значение из age и сохраняет его в age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog = Dog('Willy', 5)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lesli', 3)
your_dog.sit()
your_dog.roll_over()