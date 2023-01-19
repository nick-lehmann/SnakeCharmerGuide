# ===============
# Slide 1: Basics
# ===============
class Student:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return str(self)

students = [
    Student(name="Nick", age=25),
    Student(name="Johanna", age=21),
    Student(name="Annelies", age=61),
    Student(name="Max", age=26)
]
# Fails because we can't compare two students in an unambiguous way
# print(sorted(students))



# ====================
# Slide 2: Sort by age
# ====================

# Sort by age 💡
students_by_age = sorted(students, key=lambda student: student.age)
print(students_by_age)
# => [Johanna (21), Nick (25), Max (26), Annelies (61)]


# ====================
# Slide 3: Sort by elo
# ====================
# Students by elo
season1 = {
    "Nick": 1000,
    "Johanna": 1200,
    "Annelies": 800,
    "Max": 900
}
season2 = {
    "Nick": 1100,
    "Johanna": 1300,
    "Annelies": 1500,
    "Max": 1000
}
ranking1 = sorted(students, key=lambda student: season1[student.name])
# this is just a function 🧐 ---^ 
ranking2 = sorted(students, key=lambda student: season2[student.name])
print(ranking1)
# => [Annelies (61), Max (26), Nick (25), Johanna (21)]
print(ranking2)
# => [Max (26), Nick (25), Johanna (21), Annelies (61)]


# ============================================
# Slide 4: Sort by elo with "normal" functions
# ============================================
def get_game1_elo(name):
    return season1[name]

def get_game2_elo(name):
    return season2[name]


ranking1 = sorted(students, key=lambda student: season1[student.name])
ranking2 = sorted(students, key=lambda student: season2[student.name])
print(ranking1)
# => [Annelies (61), Max (26), Nick (25), Johanna (21)]
print(ranking2)
# => [Max (26), Nick (25), Johanna (21), Annelies (61)]




# ======================================================
# Slide 5: Sort by averageness (distance to average elo)
# ======================================================
def get_game1_averageness(student: Student) -> float:
    total_elo = sum(season1.values())
    number_of_players = len(season1)
    average_elo = total_elo / number_of_players

    player_elo = season1[student.name] 
    return abs(player_elo - average_elo)


def get_game2_averageness(student: Student) -> float:
    total_elo = sum(season2.values())
    number_of_players = len(season2)
    average_elo = total_elo / number_of_players

    player_elo = season2[student.name] 
    return abs(player_elo - average_elo)


ranking1 = sorted(students, key=get_game1_averageness)
ranking2 = sorted(students, key=get_game2_averageness)
print(ranking1)
# => [Nick (25), Max (26), Annelies (61), Johanna (21)]
print(ranking2)
# => [Johanna (21), Nick (25), Max (26), Annelies (61)]



# ============================================================================
# Slide 6: Sort by averageness (distance to average elo) with "cool" functions
# ============================================================================
from typing import Callable
def get_scorer(elo: dict[str, int]) -> Callable[[Student], float]:
    def get_averageness(student: Student) -> float:
        total_elo = sum(elo.values())
        number_of_players = len(elo)
        average_elo = total_elo / number_of_players

        player_elo = elo[student.name] 
        return abs(player_elo - average_elo)
    
    return get_averageness


scorer_game1 = get_scorer(season1)
scorer_game2 = get_scorer(season2)

ranking1 = sorted(students, key=scorer_game1)
ranking2 = sorted(students, key=scorer_game2)
print(ranking1)
# => [Nick (25), Max (26), Annelies (61), Johanna (21)]
print(ranking2)
# => [Johanna (21), Nick (25), Max (26), Annelies (61)]



# Slide 7: Sort by averageness (distance to average elo) with "cool" functions & closures
# from typing import Callable
# def get_scorer(elo: dict[str, int]) -> Callable[[Student], float]:
#     total_elo = sum(elo.values())
#     number_of_players = len(elo)
#     average_elo = total_elo / number_of_players

#     def get_averageness(student: Student) -> float:
#         player_elo = elo[student.name] 
#         return abs(player_elo - average_elo)
    
#     return get_averageness


# scorer_game1 = get_scorer(elo1)
# scorer_game2 = get_scorer(elo2)

# ranking1 = sorted(students, key=scorer_game1)
# ranking2 = sorted(students, key=scorer_game2)
# print(ranking1)
# # => [Nick (25), Max (26), Annelies (61), Johanna (21)]
# print(ranking2)
# # => [Johanna (21), Nick (25), Max (26), Annelies (61)]