# Задача 2. (Уровень: средний начинающий)
'''
Тема: Циклы, списки, строки.
Дана строка, состоящая из слов, разделенных пробелами.
Напишите программу, которая возвращает новую строку, где каждое слово перевернуто (задом наперед), но порядок слов сохранен.
'''

st = "hello world python"
sp = st.split(' ')  

reversed_words = []
for word in sp:
    reversed_word = word[::-1]  
    reversed_words.append(reversed_word)

result = " ".join(reversed_words) 
print(result) 