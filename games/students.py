"""
You have a course with students, each having a "name", an "age" and a list of "grades", e.g.:

```python
students = [
  {
    'name': 'John',
    'age': 21,
    'grades': [1.3, 2.7, 1.0]
  },
  {
    'name': 'Michelle',
    'age': 25,
    'grades': [1.0, 3.7, 2.3]
  },
  {
    'name': 'Thomas',
    'age': 41,
    'grades': [2.3, 2.7, 2.0]
  }
]
```

(It is best to put the information in a variable, don't use `input()` here)

And now you want to gather some information about your course. It is enough to print the information to the console after each other.

1) For your teaching, you need a list of names sorted alphabetically.
2) Your memory got quite bad as you have grown older. Is there a 'Thomas' in your course?
3) Since your students vary in age, you want to know the average age of your class.
4) Some students perform better, some worse. You would like to know the average grade of each student.
   Bonus: Print the student names sorted by their average grade.
5) Ah shit, the other class is better than yours. To make you look like a better teacher, you decide to remove the worst grade for each student. Do so and print their averages again.
6) Now, you notice that some students are still not doing well. You want to print the names of all students (like in task 3) with an average grade bigger than 2.0.
   Bonus: In case you made a function to print the average, try to do this without changing the former function calls.
"""

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

# 1) Sort names
names = []
for student in students:
  names += [student['name']]

print("Your students:")
for name in sorted(names):
  print(f"- {name}")

# 2) Is there a Thomas?
print("Is there a Thomas? ", "Thomas" in names)
# Hint: Ternary: "Yes" if "Thomas" in names else "No"

# 3) Average age
cumulative_age = 0
for student in students:
  cumulative_age += student['age']
print("Average age of students:", cumulative_age / len(students))

# Print students with average grade above 2.0
def print_averages(students, threshold=None):
  for student in students:
    total_score = 0
    for grade in student['grades']:
      total_score += grade
    average_score = total_score / len(student['grades'])
    
    if threshold and average_score > threshold:
      continue
    
    print(f"{student['name']} has an average grade of {average_score}")

print("Good students are:")
print_averages(students)

# Remove worst grade
for student in students:
  worst_grade = 0
  for grade in student["grades"]:
    if grade > worst_grade:
      worst_grade = grade

  # Alternative:
  # worst_grade = max(student["grades"])

  student["grades"].remove(worst_grade)

print("Now good students are:")
print_averages(students, threshold=2.0)