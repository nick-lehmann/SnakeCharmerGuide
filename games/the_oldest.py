"""
You have some students and know how old they are. Mike is 19, Peter is 20, Michelle is 22 and Nicole is 20.

1. Save the age of each student in a dictionary.
2. Add the student Max who is 18 years old.
3. Today is Michelle's birthday, so make Michelle her one year older.
4. Choose a name and check if there is a student with this name.
5. Find the oldest student and print his name and age.
"""

students = {
    'Mike': 19,
    'Peter': 20,
    'Michelle': 22,
    'Nicole': 20
}

students['Max'] = 18
students['Michelle'] += 1


name = input('Name of student?🙋🏼‍️: ')

if name in students:
    print(f"We have a student who's name is {name}")
else:
    print(f'There is no such thing as a {name}')


oldest_age = 0
oldest_name = 0
for student, age in students.items():
    if age > oldest_age:
        oldest_age = age
        oldest_name = student

print(f'The oldest student is {oldest_name} who is {oldest_age}')
