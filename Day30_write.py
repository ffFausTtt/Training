# JSON
from pathlib import Path
import json

numbers = [2, 4, 6, 8, 10, 12]

path = Path('numbers.json') # Задаем название файла для хранения списка. Обычно используется расширение  .json
# Функция json.dumps - используется для генерации строки, содержащей JSON-представление обрабатываемых данных
contents = json.dumps(numbers) 
path.write_text(contents)