from pathlib import Path

path = Path('Day26_pi.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Запись в файл
path = Path('Day27_programming.txt')
path.write_text("Hello World!")
'''
write_text() - если файла не существует, он создается. Если файл уже создан - он переписывается
'''
# Запись нескольких строк
contents = 'Games '
contents += 'Guitar '
contents += 'Sport'

path.write_text(contents)