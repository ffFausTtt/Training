from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text() # Считываем файл
numbers = json.loads(contents) # Передаем содержимое в функцию json.loads, которая принимает строку в формате JSON и возвращает Python-объект

print(numbers)