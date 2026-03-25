class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.coffee_beans = 500
        self.milk = 300
        
        self.recipes = {
            "эспрессо": {"water": 50, "coffee_beans": 15, "milk": 0},
            "американо": {"water": 100, "coffee_beans": 15, "milk": 0},
            "латте": {"water": 50, "coffee_beans": 15, "milk": 100}
        }
    
    def make_coffee(self, drink_name):
        """Готовит напиток, если достаточно ресурсов"""
        drink_name = drink_name.lower()
        
        if drink_name not in self.recipes:
            return f"Напиток '{drink_name}' не найден в меню"
        
        can_make, message = self.check_resources(drink_name)
        
        if not can_make:
            return message
        
        recipe = self.recipes[drink_name]
        self.water -= recipe["water"]
        self.coffee_beans -= recipe["coffee_beans"]
        self.milk -= recipe["milk"]
        
        return f"{drink_name.capitalize()} готов! Приятного аппетита!"
    
    def add_water(self, amount):
        """Добавляет воду"""
        if amount > 0:
            self.water += amount
            return f"Добавлено {amount} мл воды. Теперь воды: {self.water} мл"
        return "Количество должно быть положительным"
    
    def add_coffee(self, amount):
        """Добавляет кофе"""
        if amount > 0:
            self.coffee_beans += amount
            return f"Добавлено {amount} г кофе. Теперь кофе: {self.coffee_beans} г"
        return "Количество должно быть положительным"
    
    def add_milk(self, amount):
        """Добавляет молоко"""
        if amount > 0:
            self.milk += amount
            return f"Добавлено {amount} мл молока. Теперь молока: {self.milk} мл"
        return "Количество должно быть положительным"
    
    def get_status(self):
        """Возвращает строку с текущим уровнем всех ресурсов"""
        return f"Вода: {self.water} мл, Кофе: {self.coffee_beans} г, Молоко: {self.milk} мл"
    
    def check_resources(self, drink_name):
        """Проверяет, достаточно ли ресурсов для приготовления напитка"""
        drink_name = drink_name.lower()
        
        if drink_name not in self.recipes:
            return False, f"Напиток '{drink_name}' не найден"
        
        recipe = self.recipes[drink_name]
        missing_resources = []
        
        if self.water < recipe["water"]:
            missing_resources.append(f"вода (нужно {recipe['water']} мл, есть {self.water} мл)")
        
        if self.coffee_beans < recipe["coffee_beans"]:
            missing_resources.append(f"кофе (нужно {recipe['coffee_beans']} г, есть {self.coffee_beans} г)")
        
        if self.milk < recipe["milk"]:
            missing_resources.append(f"молоко (нужно {recipe['milk']} мл, есть {self.milk} мл)")
        
        if missing_resources:
            return False, f"Недостаточно ресурсов: {', '.join(missing_resources)}"
        
        return True, "Ресурсов достаточно"


if __name__ == "__main__":
    machine = CoffeeMachine()
    
    print("Статус кофемашины")
    print(machine.get_status())
    print()
    
    print("Готовим латте")
    result = machine.make_coffee("латте")
    print(result)
    print(machine.get_status())
    print()
    
    print("Готовим несколько эспрессо")
    for i in range(3):
        result = machine.make_coffee("эспрессо")
        print(result)
    print(machine.get_status())
    print()
    
    print("Попытка приготовить латте без ресурсов")
    result = machine.make_coffee("латте")
    print(result)
    print()
    
    print("Добавляем ресурсы")
    print(machine.add_water(500))
    print(machine.add_coffee(200))
    print(machine.add_milk(150))
    print()
    
    print("Проверка ресурсов для американо")
    can_make, msg = machine.check_resources("американо")
    print(msg)
    print()
    
    print("Готовим американо")
    result = machine.make_coffee("американо")
    print(result)
    print(machine.get_status())
    print()

    print("Попытка приготовить капучино")
    result = machine.make_coffee("капучино")
    print(result)