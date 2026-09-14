def student_result(name, marks1, marks2, marks3):
    print(f"Name: {name}")
    print(f"Total Marks: {marks1+marks2+marks3}")
    print(f"Percentage: {(((marks1+marks2+marks3)/300)*100):.2f}%")

student_result("SP",60,90,79)