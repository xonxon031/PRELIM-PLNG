while True:
    java_score = float(input("Java Score: "))
    c_score = float(input("C Score: "))
    db_score = float(input("Database Handling score: "))

    average = (java_score + c_score + db_score) / 3.0

    if 90 <= average <= 100:
        grade = "A"
    elif 80 <= average < 90:
        grade = "B"
    elif 75 <= average < 80:
        grade = "C"
    else:
        grade = "F"

    print("Output:")
    print(grade)
    print("Explanation:")
    print(
        f"The average of the student is {average:.3f}, so the student's grade is {grade}."
    )

    choice = input("Do you want to continue: YES / NO\n").strip().upper()
    if choice != "YES":
        break