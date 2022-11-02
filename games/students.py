students = [
  {
    'name': 'Michelle',
    'age': 25,
    'grades': [1.0, 3.7, 2.3]
  },
  {
    'name': 'Thomas',
    'age': 41,
    'grades': [2.3, 2.7, 2.0]
  },
  {
    'name': 'John',
    'age': 21,
    'grades': [1.3, 2.7, 1.0]
  },
]

# 1) Print names
print('\n1)\n')

names = []
for student in students:
  names += [student['name']]

print("Your students:")
for name in names:
  print(f"- {name}")

# 2) Is there a Thomas?
print('\n2)\n')

print("Is there a Thomas? ", "Thomas" in names)
# Hint: Ternary: "Yes" if "Thomas" in names else "No"

# 3) Average age
print('\n3)\n')

cumulative_age = 0
for student in students:
  cumulative_age += student['age']
print("Average age of students:", cumulative_age / len(students))

# 4) Average grade
print('\n4)\n')

def calculate_averages():
  for student in students:
    total = 0
    for grade in student['grades']:
      total += grade
    average = total / len(student['grades'])
    student['average'] = average

def print_grades(filter=None):
  for student in students:
    if filter and filter < student['average']:
      continue
    print(f"{student['name']} has an average grade of {student['average']:.1f}")

calculate_averages()
print_grades()

# 5) Remove worst grade
print('\n5)\n')

def remove_worst_grade():
  for student in students:
    worst_grade = 0
    for grade in student['grades']:
      if grade > worst_grade:
        worst_grade = grade
    student['grades'].remove(worst_grade)

remove_worst_grade()
calculate_averages()
print_grades()

# 6) Print the "good" students
print('\n6)\n')

print_grades(2.0)
