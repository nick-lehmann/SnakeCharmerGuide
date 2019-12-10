"""
1) Implement a class Human class with just the attributes `name` and `age`. Do not forget the constructor.
2) Add a method for saying hi. It should print out the name and the age.
3) Add a method for having birthday that increases the age of the current human by one.
4) Add a list of hobbies to your Human class (remember the constructor) and include the hobbies in the say_hi method.
5) Add a method has_hobby to find out, if the given hobby is one of the humans hobbies. Return a True or False.
6) Add a method to add a humans hobby. If the human already has the hobby, print an appropriate message and do not add
   it. Otherwise, add it.

Bonus: Inheritance! If your are really fast and feel comfortable with object-oriented programming in Python, have a look
    at this [short introduction to inheritance](https://github.com/nick-lehmann/SnakeCharmerGuide/blob/master/docs/code/class_inheritance.py).
    Try to implement a subclass of Human that represents a Student. Add an attribute that represents his or her student
    id and change the method for saying hi to also print the student id at the end.
"""


class Human:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def say_hi(self):
        print(f'Hi, I am {self.name} and {self.age} years old! 👋🏻')
        for hobby in self.hobbies:
            print(f'  - {hobby}')

    def birthday(self):
        self.age += 1
        print(f'{self.name} is now {self.age} years old 🎂')

    def has_hobby(self, hobby):
        # for h in self.hobbies:
        #     if h == hobby:
        #         return True
        # return False
        return hobby in self.hobbies

    def add_hobby(self, hobby):
        if self.has_hobby(hobby):
            print(f'{self.name} already has {hobby} as a hobby')
            return

        self.hobbies.append(hobby)


class Student(Human):
    def __init__(self, name, student_id, age, hobbies):
        super().__init__(name, age, hobbies)
        self.student_id = student_id

    def say_hi(self):
        super().say_hi()
        print(f'Student id: {self.student_id}')


student = Student('Peter', '4242', 21, ['Swimming', 'Hiking'])
student.say_hi()

