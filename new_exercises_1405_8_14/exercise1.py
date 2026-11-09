def Safe_Division():
    try:
        number1 = int(input())
        number2 = int(input())
        answer = number1 / number2
        print(answer)
    
    except ZeroDivisionError:
        print("you can't use zero for second num !!")

    except ValueError:
        print("you can't use this valid !!")

    except Exception: 
        print("error")
        
    finally:
        print("Operation completed")

result = Safe_Division()