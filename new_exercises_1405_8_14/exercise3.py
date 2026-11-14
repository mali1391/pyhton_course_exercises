def list_index_access():
    try:
        drinks_list = ["pepsi", "coca cola", "fanta", "shani", "hype"]
        my_index = int(input(f"which drink do you want? {drinks_list}if you want first index please enter 0: "))
        
        result = drinks_list[my_index]
        print(result)

    except ValueError:
        print("your choice isn't integer !!")

    except IndexError:
        print("your index is wrong")

    except Exception:
        print("your choice is not correct")

    else:
        print("program runs seccessful")

result = list_index_access()