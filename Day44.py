# Задача: "Система управления заказами в кафе"

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.available = True

    def __str__(self):
        return f"{self.name} - {self.price} руб."
    
    def toogle_availability(self):
        if self.available == True:
            self.available = False
        else: 
            self.available = True


class Order: 
    def __init__(self, order_id):
        self.order_id = order_id
        self.spisok = []
        self.total_price = 0
        self.status = "в работе"

    def add_item(self, menu_item, cost):
        self.spisok.append(menu_item)
        self.total_price += cost

    def remove_item(self, menu_item, cost):
        self.spisok.remove(menu_item)
        self.total_price -= cost

    def complete_order(self):
        self.status = "готов"

    def __str__(self):
        return f"Number: {self.order_id}\nOrder: {self.spisok}\nPrice: {self.total_price}\nStatus: {self.status}"
