class Fish:
    def __init__(self, species='Fish', size=1):
        self.species = species
        self.size = float(size)

    def swim(self):
        print("I can swim! 🐟")

    def what_am_i(self):
        print(f'I am a {self.size} meter long {self.species}')


class Salmon(Fish):
    """
    Here the class Salmon inherits (also called extends) the class Fish.
    When inheriting (or extending) a class, the new class gets all the methods and attributes the original class had.
    In this case the what_am_i and swim methods.
    This way we can build upon existing classes like building blocks or legos.
    """

    def __init__(self, size):
        super().__init__('Salmon', size)
        self.expensive = True

    def what_am_i(self):
        """
        Optionally you can add functionality to existing methods
        """
        super().what_am_i()
        print('Plus something else')

    def swim_backwards(self):
        """
        Or simply add new methods
        """
        print(f'I am a Salmon, I can even swim backwards! 🐠')


nemo = Fish()
nemo.swim()
nemo.what_am_i()

not_nemo = Salmon(3)
not_nemo.swim()
not_nemo.swim_backwards()
not_nemo.what_am_i()
print(f'Expensive: {not_nemo.expensive}')
