message = "Hello Word!"     
print(message)      

message = "Goodby Word!"    
print(message)     

name = 'Artyom' 
print(f"Hi {name}")
print(name.title(), name.upper(), name.lower())     #Все изменения временные. Для постоянства необходимо перезаписать, например: name = name.upper()
#title() - первые символы в верхнем регистре;   upper() - все символы в верхнем регистре;    lower() - все символы в нижнем регистре. 

author = "Дзен-монах"
talk = '"Это просто пустая лодка"'
print(f"{author} однажды сказал: {talk}")

message = f"{author} однажды сказал: {talk}"
print(message)

person = "      Artyom      Moskalenko            "
print(person.rstrip() + "\n" + person.lstrip() + "\n" + person.strip())     #Все изменения временные. Для постоянства необходимо перезаписать, например: person = person.strip()
#rstrip() - удаление пробельных символов СПРАВА;  lstrip() - удаление пробельных символов СЛЕВА;    strip() - удаление пробельных символов со всех концов.

file = "ttt:day1.exe"   #Все изменения временные. Для постоянства необходимо перезаписать, например: file = file.removeprefix()
#removeprefix() - удаление префикса;     removesuffix() - удаление суффикса.
print(file.removeprefix("ttt:"))
print(file.removesuffix(".exe"))
print(file)