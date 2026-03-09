from pathlib import Path
import json

class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author 
        self.year = year
        self.read = read

    def mark_as_read(self):
        self.read = True

    def get_info(self):
        status = ''
        if self.read == True:
            status = 'Прочитана'
        else: 
            status = 'Не прочитана'
        all_book = f"{self.title}|{self.author}({self.year}) - {status}" 
        return all_book

    def to_dict(self): 
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'read': self.read
        }


def add_book(collection, title, author, year):
    book = Book(title, author, year) 
    collection.append(book)
    return collection

def find_books_by_author(collection, author):
    collection_by_author = []
    for book in collection:  
            collection_by_author.append(book)
   
    return collection_by_author

def unread_books(collection): 
    unread = []
    for book in collection:
        if book.read == False:
            unread.append(book)
    
    return unread

def save_collection(collection, filename):
    books_data = [book.to_dict() for book in collection]  
    path = Path(filename)
    content = json.dumps(books_data, ensure_ascii=False, indent=2)  
    path.write_text(content, encoding='utf-8')  
    print(f"✅ Сохранено {len(collection)} книг")

def load_collection(filename):
    path = Path(filename)
    content = path.read_text(encoding='utf-8') 
    books_data = json.loads(content)
    
    collection = [] 
    for book_data in books_data:
        book = Book(
            book_data['title'],
            book_data['author'],
            book_data['year'],
            book_data['read']
        )
        collection.append(book)
    
    print(f"✅ Загружено {len(collection)} книг")
    return collection


# Тестирование
my_books = []

my_books = add_book(my_books, "Война и мир", "Л. Толстой", 1869)
my_books = add_book(my_books, "Преступление и наказание", "Ф. Достоевский", 1866)
my_books = add_book(my_books, "Мастер и Маргарита", "М. Булгаков", 1967)

my_books[0].mark_as_read()

print("\n=== Все книги ===")
for book in my_books:
    print(book.get_info())

dostoevsky_books = find_books_by_author(my_books, "Ф. Достоевский")
print(f"\nНайдено книг Достоевского: {len(dostoevsky_books)}")

to_read = unread_books(my_books)
print(f"Нужно прочитать: {len(to_read)}")

save_collection(my_books, "books.json")
loaded = load_collection("books.json")
print(f"Загружено книг: {len(loaded)}")

# Проверка загруженных
if loaded:
    print("\n=== Проверка загруженных ===")
    print(loaded[0].get_info())