import os

def file_reader():

    try:
        file_name = input("please enter your file address: ")
        
        os.path.exists(file_name)
        file = open(file_name)
        content = file.read()
        print(content)

    except FileNotFoundError:
        print("file not found !!")

    except  PermissionError:
        print("you can't see this file")

    except Exception:
        print("you wrote the address wrong !!")

file_reader()