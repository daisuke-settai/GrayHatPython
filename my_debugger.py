from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass

    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS  # CREATE_NEW_CONSOLEでGUI
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        
        # 起動プロセスを別ウィンドウで表示
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe.encode('utf-8'), None, None, None, None, \
             creation_flags, None, None, byref(startupinfo), byref(process_information)):
            print("[*] We have successfully launched the process!")
            print("[*] PID: {}".format(process_information.dwProcessId))

        else:
            print("[*] Error: 0x{:08x}.".format(kernel32.GetLastError()))