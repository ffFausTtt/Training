# Чтение всего файла 
from pathlib import Path

path = Path('Day26_pi.txt') # Относительный путь используется если текстовый и выполняемый файл находятся в одном каталоге
# Абсолютный путь - найдет в любом каталоге системы: 
# path = Path('/Users/admin/github_traning/Training/Day26_pi.txt')
contents = path.read_text()#.strip() - можно вызывать подряд
print(contents)

contents = contents.strip() # Функции для форматирования строк также применимы
print(contents)

# Построчное считывание
lines = contents.splitlines()
for line in lines:
    print(f"{line}\n")