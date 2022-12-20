from pymem import *

dll_path = input("Enter the DLL path: ")
dll_path_bytes = bytes(dll_path, "UTF-8")
process_name = input("Enter the process name: ")

open_process = Pymem(process_name)
process.inject_dll(open_process.process_handle, dll_path_bytes)

print("DLL injected successfully!")
input()
