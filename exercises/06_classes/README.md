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
