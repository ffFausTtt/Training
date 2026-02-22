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

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.descriptive())
my_new_car.odometer = 23 # Прямое изменение значения атрибута
my_new_car.update_odometer(86)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2018)
print(my_used_car.descriptive())
my_used_car.update_odometer(234)
my_used_car.read_odometer()
my_used_car.increment_odometer(54)
my_used_car.read_odometer()