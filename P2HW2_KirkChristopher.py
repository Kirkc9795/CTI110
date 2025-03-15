#Christopher Kirk
#03/15/2025
#P2HW2
# I am making a grading calculator

module_grades = []


grade1 = float(input("Enter your grade for Module 1: "))
module_grades.append(grade1)

grade2 =int(input("Enter your grade for Module 2: "))
module_grades.append(grade2)

grade3 = float(input("Enter your grade for Module 3: "))
module_grades.append(grade3)

grade4 = int(input("Enter grade for Module 4:"))
module_grades.append(grade4)

grade5 = int(input("Enter grade for Module 5:"))
module_grades.append(grade5)

grade6 = int(input("Enter grade for Module 6:"))
module_grades.append(grade6)
 
average_grade = sum(module_grades) /len(module_grades)

print("------------Results------------")

print("Grades entered:", module_grades)
print("Lowest Grade: ", min(module_grades))
print("Highest Grade: ", max(module_grades))
print("Sum of Grades:", sum(module_grades))
print(f"Average Grade: {average_grade:.2f}")

print("----------------------------------------")
