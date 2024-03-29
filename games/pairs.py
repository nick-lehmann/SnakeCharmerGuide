"""
All the students must get together in groups to complete a task.
After getting into groups, is there anyone alone or an incomplete group?

1. Define a variable "students" and one "group_size"
2. Check with the modulo operator "%" if there is someone left out if the group

Bonus Points: How many additional students do you need to fill the group?
Bonus Bonus Points: What group sizes are possible so that no one is left out?
"""

students = 50
group_size = 3

alone = 50 % 3

if alone == 0:
    print('Everyone has group!')
else:
    print(f'{alone} people are alone 😢')
    print(f'We need {group_size - alone} more students')

    # Find the perfect group sizes
    for i in range(1, students):
        if students % i == 0:
            print(f"{i} is a perfect group size")
