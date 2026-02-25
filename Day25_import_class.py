from Day25 import Car # Можно импортировать сразу несколько, перечислив их через запятую import Car, ElectronicCar 
my_new_car = Car('audi', 'a4', 2025) 
print(my_new_car.descriptive())
my_new_car.odometer = 55
my_new_car.read_odometer()


from Day25 import ElectronicCar
my_leaf = ElectronicCar('nissan', 'leaf', '2024')
print(my_leaf.descriptive())
my_leaf.battery.battery_size = 40
my_leaf.battery.get_range()

# Импортирование модуля целиком: import Day25
# Импортирование всех классов из модуля: from Day25 import *
# Импортирование модуля в модулю:
'''
from Day25 import Car - сразу импортируем класс-родитель, т.к. классу-наследнику необходим доступ к классу-родителю
from Day25 import ElectricCar - потом импортируем класс-наследник
'''

# Использование псевдонимов как и везде через as
from Day25 import Battery as bat
my_battery = bat()
my_battery.read_battery()
# Псевдонимы также можно присваивать модулям: import Day25 as d