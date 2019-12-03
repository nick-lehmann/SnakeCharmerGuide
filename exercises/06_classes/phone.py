"""
Phone 📱

In this exercise, we create a class that will represent a very basic phone (no WhatsApp, just calling).

The class phone gets initialized with a number and saves this number.
You can call the number, but only if it's valid.
A phone number is considered valid if it starts with a zero and it has 11 digits.
Also, you don't want to get disturbed while eating ice cream, so you can turn on don't disturb mode.
The method "ring" only rings your phone if do not disturb is off. You should be able to turn not disturb mode on and off.

Specifically, the phone class should have:
- an attribute (e.g. number) that stores its number
- an attribute (e.g. dont_disturb) that states if the phone is silent
- a method call that takes another phone number and calls it if the phone number is valid. Return a boolean
  that indicates if the call was successful.
- a method verify that takes a phone number and checks if its valid or not.
- a method mute that enables the "do not disturb" mode
- a method unmute that disables the "do not disturb" mode
- a method ring that lets the phone ring, but only if the "do not disturb" mode is disabled

Bonus: Raise an exception when constructing a phone and the number is not valid.
"""
import unittest


class Phone:
    pass


class PhoneTestCase(unittest.TestCase):
    def setUp(self):
        self.phone_one = Phone('01234567890')
        self.phone_two = Phone('09876543210')

    def test_call_valid_phone_number(self):
        self.assertTrue(self.phone_one.call('01212121212'))

    def test_call_invalid_phone_number(self):
        self.assertFalse(self.phone_one.call(''))
        self.assertFalse(self.phone_one.call('0'))
        self.assertFalse(self.phone_one.call('1'))
        self.assertFalse(self.phone_one.call('01111'))
        self.assertFalse(self.phone_one.call('073478'))
        self.assertFalse(self.phone_one.call('0123456789'))

    def test_normal_call(self):
        self.assertTrue(self.phone_one.call(self.phone_two.number))
        self.assertTrue(self.phone_two.ring())

    def test_call_with_do_not_disturb(self):
        self.phone_two.mute()
        self.assertTrue(self.phone_one.call(self.phone_two.number))
        self.assertFalse(self.phone_two.ring())

        self.phone_two.unmute()
        self.assertTrue(self.phone_one.call(self.phone_two.number))
        self.assertTrue(self.phone_two.ring())


unittest.main()
