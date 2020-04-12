from ctypes import *

libc = CDLL("libc.so.6")
message_string = "Hello world!\n"
libc.printf("Testing: %s".encode('utf-8'), message_string.encode('utf-8'))