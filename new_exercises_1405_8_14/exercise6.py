import json

class MissingConfigurationError(Exception):
    pass

def JSON_Configuration_Reader():
    try:

        json_file = input("enter your json file: ")
        with open(json_file) as file:
            config = json.load(file)

        required_keys = ["user_name", "password", "port", "debug"]

        for key in required_keys:
            if key not in config:
                raise MissingConfigurationError(f"MissingConfigurationError: {key}")

        print("configuration loaded successfully !!")
        print(config)

    except FileNotFoundError:
        print("program can't find your file !!")

    except json.JSONDecodeError:
        print("invalid json format !!")

    except MissingConfigurationError as e: 
        print(f"error : {e}")
        
JSON_Configuration_Reader()