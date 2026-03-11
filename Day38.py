# Задача: «Тренировки и упражнения»

from datetime import date

class Workout:
    def __init__(self, name, duration, calories, difficulty):
        self.name = name
        self.duration = duration
        self.calories = calories
        self.date = str(date.today())
        self.difficulty = difficulty
    
    def get_info(self):
        all_str = f"{self.name} | {self.duration} | {self.calories} | {self.difficulty} | {self.date}"
        return all_str

    def to_dict(self):
        return {
            'name': self.name,
            'duration': self.duration, 
            'calories': self.calories,
            'difficulty': self.difficulty,
            'date': self.date
        } 
    


def add_workout(workouts, name, duration, calories, difficulty):
    new_workout = Workout(name, duration,calories, difficulty)
    workouts.append(new_workout)
    return workouts

def find_by_name(workouts, name):
    for work in workouts:
        if work.name == name:
            return work
    return None

def filter_by_difficulty(workouts, difficulty):
    result = [] 
    
    for work in workouts:
        if work.difficulty == difficulty: 
            result.append(work) 
    
    return result 

my_workouts = []


my_workouts = add_workout(my_workouts, name = "Бег", duration = 30, calories = 300, difficulty = "средняя")
my_workouts = add_workout(my_workouts, "Плавание", 45, 400, "легкая")
my_workouts = add_workout(my_workouts, "Йога", 60, 200, "тяжелая")
my_workouts = add_workout(my_workouts, "Велосипед", 50, 500, "средняя")


filter_by_difficulty(my_workouts, "сложная")