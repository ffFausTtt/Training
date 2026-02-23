class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 # Значение по умолчанию
    
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


# Наследование
class ElectronicCar(Car):
    def __init__(self, make, year, model):
        super().__init__(make, model, year) # super - специальная функция позволяющая вызвать метод родительского класса
        
        # Определение атрибутов и методов класса-потомка
        self.battery_size = 40 

    def read_battery(self):
        print(f"Battery: {self.battery_size}-kWh")    


my_leaf = ElectronicCar('nissan', 'leaf', 2024)
print(my_leaf.descriptive())
my_leaf.read_battery()