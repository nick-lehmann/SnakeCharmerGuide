# 1
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.greet()

    def greet(self):
        return f'Hi, I am {self.name} and {self.age} years old! 👋'

    def birthday(self):
        self.age += 1
        print(f'{self.name} is now {self.age} years old 🎂')

# 2
class Student(Human):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    # Overrides the greet method from the Human class.
    def greet(self):
        human = super().greet()
        return f'{human} I am a student at {self.school}!'

    def take_notes(self):
        print(f'{self.name} is taking notes 📝')


# 3
class Teacher(Human):
    def __init__(self, name, age, school, subject):
        super().__init__(name, age)
        self.school = school
        self.subject = subject

    # Overrides the greet method from the Human class.
    def greet(self):
        human = super().greet()
        return f'{human} I teach {self.subject} at {self.school}.'

    def teach(self):
        print(f'{self.name} is teaching {self.subject} 📚')


# 4
def is_classroom_complete(classroom):
    has_teacher = False
    students = 0
    for student in classroom:
        if isinstance(student, Teacher):
            has_teacher = True
        elif isinstance(student, Student):
            students += 1
        else:
            return False
    return has_teacher and students >= 2


# 5
def hold_class(classroom):
    for human in classroom:
        if isinstance(human, Student):
            human.take_notes()
        elif isinstance(human, Teacher):
            human.teach()
        else:
            print('I am not a teacher or a student 😢')


# BONUS
class ClassRoom:
    def __init__(self):
        self.students = []
        self.teacher = None
        
    def add_human(self, human):
        if isinstance(human, Teacher):
            self.teacher = human
        elif isinstance(human, Student):
            self.students.append(human)
        else:
            print('ALARM!!!!')

    def hold_class(self):
        if self.teacher is None:
            print('No teacher, no class!')
            return

        if len(self.students) < 2:
            print('Not enough students, definitely not worth!')
            return

        self.teacher.teach()
        for student in self.students:
            student.take_notes()


# RUN
alma = Human('alma', 20)
print(alma)
alma.birthday()

bob = Student('bob', 21, 'TU Dresden')
print(bob)
bob.birthday()

carla = Student('carla', 22, 'TU Dresden')

nicco = Teacher('nicco', 26, 'TU Dresden', 'Python')
print(nicco)

# 4 & 5
classroom = [bob, carla, nicco]
if is_classroom_complete(classroom):
    print('We can start!')
else: 
    print('Something is wrong...')
hold_class(classroom)

# BONUS
classroom = ClassRoom([bob, carla, nicco])
classroom.hold_class()
