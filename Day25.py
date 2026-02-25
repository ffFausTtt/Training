'''Класс для представления автомобиля'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 # Значение по умолчанию
        self.gas_tank = 95

    def descriptive(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"Probeg: {self.odometer} miles")

    # Изменение значения атрибута с помощью метода
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else: print("You can't roll mack an odometer")
    
    # Изменение значения атрибута с приращением
    def increment_odometer(self, miles):
        self.odometer += miles

    def fill_gas_tank(self):
        print(f"This car does a gas tank: {self.gas_tank}")


# Хранение нескольких классов в модуле 
class Battery:
    def __init__(self,battery_size = 40):
        self.battery_size = battery_size
    def read_battery(self):
        print(f"Battery: {self.battery_size}-kWh")  
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")

class ElectronicCar(Car):
    def __init__(self, make, year, model):
        super().__init__(make, model, year) # super - специальная функция позволяющая вызвать метод родительского класса
        
        # Определение атрибутов и методов класса-потомка
        # self.battery_size = 40 

        # Экземпляр класса как атрибут
        self.battery = Battery() # Даем указание создать новый экземпляр Battery

    # Переопределение методов класса родителя 
    def fill_gas_tank(self): # В классе потомке определяется метод с таким же названием 
        print("This car doesn't a gas tank")  