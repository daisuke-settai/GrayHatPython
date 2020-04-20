import my_debugger

debugger = my_debugger.debugger()
#debugger.load("C:\\Windows\\System32\\calc.exe")

pid = input("Enter the PID of the process to attach to: ")

debugger.attach(int(pid))
printf_address = debugger.func_resolve("msvcrt.dll", "printf")
print("[*] Address of printf: 0x{:08x}".format(printf_address))
debugger.bp_set_sw(printf_address)

debugger.run()
# list = debugger.enumerate_threads()
# for thread in list:
#     thread_context = debugger.get_thread_context(thread)
#     # レジスタ値が0しかとれない...
#     # thread_context.Eip = 111
#     print("[*] Dumping register for thread ID: 0x{:08x}".format(thread))
#     print("[**] EIP: 0x{:08x}".format(thread_context.Eip))
#     print("[**] ESP: 0x{:08x}".format(thread_context.Esp))
#     print("[**] EBP: 0x{:08x}".format(thread_context.Ebp))
#     print("[**] EAX: 0x{:08x}".format(thread_context.Eax))
#     print("[**] EBX: 0x{:08x}".format(thread_context.Ebx))
#     print("[**] ECX: 0x{:08x}".format(thread_context.Ecx))
#     print("[**] EDX: 0x{:08x}".format(thread_context.Edx))
#     print("[**] EFlags: 0x{:08x}".format(thread_context.EFlags))
#     print("[*] END DUMP")

debugger.detach()