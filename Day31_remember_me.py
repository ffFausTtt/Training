from pathlib import Path
import json 

path = Path('username.json')
if path.exists(): # Метод exists возвращает True, если файл или папка существует и False если нет 
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back {username}")
else:
    username = input("Name: ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"Your name is remember {username}")