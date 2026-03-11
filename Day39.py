mess = input("Text: ")
znaki = ".,:;/?!"  
words = []

for m in mess.split():
    clean = m.strip(znaki)
    if clean:
        words.append(clean.lower())

print("Все слова:", words)

# Уникальные слова
not_duplicate = []
for w in words:
    if w not in not_duplicate: 
        not_duplicate.append(w)

print("Уникальные:", not_duplicate)

# Самое длинное слово
long = not_duplicate[0]
for long_word in not_duplicate:
    if len(long_word) > len(long):
        long = long_word

print("Самое длинное:", long)

# Подсчет "питон"
count = 0
for w in words:
    if w == "питон":  
        count += 1

print(f"Слово 'питон' встречается: {count} раз(а)")