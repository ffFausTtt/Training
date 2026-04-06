# Задача №4
# def top_students(students, n):
#     sum = []
#     for i in students:
#         for key, value in i.items():
#             if key == 'grades':
#                 sum.append(value)
#     count = 0
#     for i in sum:
#         for j in i:
#             count += j
#             print(count)
#     print(sum)

            

def top_students(students, n):
    results = []  # будем хранить (средний_балл, имя) для каждого студента
    
    for student in students:
        name = student["name"]  # берем имя
        grades = student["grades"]  # берем список оценок
        
        average = sum(grades) / len(grades)  # вычисляем средний балл
        
        results.append((average, name))  # сохраняем пару (средний балл, имя)
    
    print(results)  # посмотрим, что получилось







students = [
    {"name": "Анна", "grades": [5, 5, 4]},
    {"name": "Иван", "grades": [3, 4, 3]},
    {"name": "Мария", "grades": [5, 5, 5]},
    {"name": "Борис", "grades": [4, 4, 4]},
]
    
print(top_students(students, 2))