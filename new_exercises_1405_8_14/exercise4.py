def students_grade_calculator():
    grades = []
    try:

        for i in range(5):
            grade = float(input("enter your grade: "))
            if grade >= 0 and grade <= 20:
                grades.append(grade)
                total = grades[i] + grades[i-1]

            else:
                raise ValueError("the grade is not correct !!")

        average = total / len(grades)
        print(f"this is the average: {average}")

    except ValueError:
        print("the grade type is wrong")
        print("please try again !!")

students_grade_calculator()