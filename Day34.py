# Задача: "Трекер привычек"

class Habit:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.streak = 0

    def done(self):
        self.streak += 1
        print(f"Привычка {self.name} выполнена! Текущая серия {self.streak}")

    def is_achieved(self):
        if self.streak >= self.goal:
            return True
        else: 
            return False
        

def save_progress(habit):
    import json
    habit_dict = {
        "name" : habit.name,
        "goal" : habit.goal,
        "sreak" : habit.streak
    }
    return json.dumps(habit_dict)

    
if __name__ == '__main__':
    my_habit = Habit("Programming", 10)

    print(my_habit.done())
    print(my_habit.done())
    print(my_habit.is_achieved())

    json_data = save_progress(my_habit)
    print(json_data)