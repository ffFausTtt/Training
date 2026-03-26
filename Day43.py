# Задача: "Банковский счет"

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else: 
            print("Error")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Ошибка: сумма должна быть положительной!")
        elif amount > self.balance:
            print(f"Ошибка: недостаточно средств! Доступно: {self.balance}") 
        else:
            self.balance -= amount
        
    def show_balance(self):
        print(f"Owner: {self.owner}\nBalance: {self.balance}")

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Ошибка: сумма должна быть положительной!")
        elif amount > self.balance:
            print(f"Ошибка: недостаточно средств! Доступно: {self.balance}") 
            
        else:
            self.balance -= amount
            other_account.deposit(amount) 


account2 = BankAccount("Tom")
account1 = BankAccount("Artyom")
account1.deposit(1000)
account1.show_balance()
account1.withdraw(500)
account1.show_balance()   
account1.transfer(100, accout2)
account1.show_balance()
account2.show_balance()