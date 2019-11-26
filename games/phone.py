# Phone 📱
# The class phone gets initialized with 1 number.
# You can call the 1 number, but only if it's valid.
# Write a method that validates the number: Valid if starts with a 0 otherwise not.

# Also, you don't want to get disturbed while eating ice cream, so you can turn on don't disturb mode.
# The method "ring" only rings your phone if do not disturb is off. You should be able to turn not disturb mode on and off


class Phone:

    def __init__(self, number):
        self.number = number
        self.dont_disturb = False

    def call(self):
        if self.verify():
            print(f'Calling {self.number} ☎️')
        else:
            print(f'Invalid number, cannot call ❌')

    def verify(self):
        return self.number[0] == '0'

    def mute(self):
        self.dont_disturb = True

    def unmute(self):
        self.dont_disturb = False

    def ring(self):
        if not self.dont_disturb:
            print('📣 Someone is calling you!')


my_first_phone = Phone('012345678')
my_first_phone.call()  # Calling
my_first_phone.ring()  # Ring
my_first_phone.mute()
my_first_phone.ring()
my_first_phone.ring()

my_first_phone = Phone('987654321')
my_first_phone.call()  # Cannot call
