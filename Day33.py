class Transaction:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description
        }

class FinanceManager:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, amount, category, description):
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        
    def get_balance(self):
        summa = 0
        for transaction in self.transactions:
            summa += transaction.amount
        return summa
    
    def get_spending_by_category(self):
        categories = {}
        for transaction in self.transactions:
            category = transaction.category
            if category not in categories:
                categories[category] = transaction.amount
            else: 
                categories[category] += transaction.amount

        return categories
    
    def save_to_file(self):

        from pathlib import Path
        import json

        path = Path('transactions.json')
        transaction_dict = []
        for transaction in self.transactions:
            transaction_dict.append(transaction.to_dict())

        contents = json.dumps(transaction_dict)
        path.write_text(contents)
        print("Сохранено!")

    def load_from_file(self):
        from pathlib import Path
        import json

        path = Path('transactions.json')
        contents = path.read_text()
        trans = json.loads(contents)

        self.transactions = []
        for trans_dict in trans:
            transaction = Transaction(
                trans_dict['amount'],
                trans_dict['category'],
                trans_dict['description']
            )
            self.transactions.append(transaction)
        
        print("Загружено!")
        for t in self.transactions:  
            print(f"{t.description}: {t.amount} ({t.category})")
        return self.transactions


manager = FinanceManager()
manager.add_transaction(3500, 'games', 'Valorant')
manager.add_transaction(500, 'food', 'Pizza')
manager.add_transaction(500, 'food', 'Hot-dog')

balance = manager.get_balance()
category = manager.get_spending_by_category()
print("По категориям: ", category)
print("Баланс: ", balance)

manager.save_to_file()
manager.load_from_file()