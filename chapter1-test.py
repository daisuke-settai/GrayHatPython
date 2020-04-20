from ctypes import *

msvcrt = cdll.msvcrt
message_string = "Hello World!\n"
str = create_string_buffer(message_string.encode('utf-8'))
msvcrt.printf("Testing: %s".encode('ascii'), str)