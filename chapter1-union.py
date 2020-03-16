from ctypes import *

class barley_amount(Union):
    _fields_ = [
        ("barley_long", c_long),
        ("barley_int", c_int),
        ("barley_char", c_char * 8),
    ]

value = input("Enter the amount of barley to put into the beer vat:")
my_barley = barley_amount(int(value))
print("Barley amount as a long: {}".format(my_barley.barley_long))
print("Barley amount as a long: {:d}".format(my_barley.barley_int))
print("Barley amount as a long: {:s}".format(my_barley.barley_char.decode('utf-8')))