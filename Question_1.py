grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Task 1

grades.sort(reverse=True)
print(grades)

# Task 2

sum_of_grades = (grades)[0] + (grades)[1] + (grades)[2] + (grades)[3] + (grades)[4] + (grades)[5] + (grades)[6] + (grades)[7] + (grades)[8] + (grades)[9]
sum_of_grades = int(sum_of_grades)
average_grade = sum_of_grades / 10
average_grade = str(average_grade)
print("The average grade is " + average_grade + ".")

# Task 3

grades[7] = "Failed"
grades[8] = "Failed"
grades[9] = "Failed"
print(grades)