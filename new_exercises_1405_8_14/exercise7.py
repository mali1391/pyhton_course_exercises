import json

class InvalidUsernameError(Exception):
    pass
class InvalidPasswordError(Exception):
    pass
class UserAccount:
    def __init__(self, enter_type):
        self.type = enter_type

class SignUpSystem:
    def __init__(self, enter_type):
        UserAccount.__init__(enter_type)

    def sign_up(self, name, password):
        try:
            users = []
            user_info = {name : password}
            users.append(user_info)

            with open("users.json", "w") as file:
                print("you sign up successful !!")
        
        except Exception as e:
            print(f"Error: {e}")

class LogInSystem(SignUpSystem):
    def __init__(self, enter_type):
        UserAccount.__init__(enter_type)

    def log_in(self, name, password):
            with open("users.json") as file:
                try:
                    saved_users = json.load(file)

                    for users in saved_users:
                        users = dict(users)

                        i = 0
                        while i < 3:
                            if i == 0:
                                for names in users:
                                    if name == names:
                                        pass
                                        
                                        for passwords in users.values():
                                            if password == passwords:
                                                print("you logged in successful !!")
                                                break
                                        break


                            if i > 0 and i < 3:
                                if name != names or passwords != password :
                                    new_name = input(f"enter your name again (remaining chance: {i}/2): ")
                                    new_password = input(f"enter your password again (remaining chance: {i}/2): ")

                                    for names in users:
                                        if new_name == names:
                                            pass

                                        elif new_name != names:
                                            pass

                                        for passwords in users.values():
                                            if new_password == passwords:
                                                pass

                                            elif new_password != passwords:
                                                pass

                                    if new_password == passwords and new_name == names:
                                        print("you logged in successful !!")
                                        # break

                            if i == 2:
                                if new_name != names:
                                    raise InvalidUsernameError("your user name is not found !!")

                                if new_password != passwords:
                                    raise InvalidPasswordError("your password is not correct !!")
                            i += 1

                except Exception as e:
                    print(f"Error: {e}")


def exhibit():
    try:
        my_type = input("do you want sign up or log in ??: ")
        program = UserAccount(my_type)

        if my_type == "sign up":
            name = input("enter your name: ")
            password = input("enter your password: ")

            SignUpSystem.sign_up(self=my_type, name=name, password=password)

        elif my_type == "log in":
            name = input("enter your name: ")
            password = input("enter your password: ")

            LogInSystem.log_in(self=my_type, name=name, password=password)

        else:
            print("error")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("program ran successful !!")

exhibit()