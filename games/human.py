class Human:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def say_hi(self):
        print(f'Hi, I am {self.name} and {self.age} years old! 👋')
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


alma = Human('alma', 20, ['code', 'bake'])
alma.say_hi()
alma.birthday()

print(alma.has_hobby('code'))

alma.add_hobby('boulder')

alma.say_hi()
