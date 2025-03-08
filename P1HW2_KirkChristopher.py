# Christopher Kirk
# 03/01/2025
# P1HW2
# This project is on basic math on numbers that are entered 
print("This program calculates and displays travel expenses" )
budget = int(input("Enter budget:"))
location = input("Enter your travel destination:")
fule = int(input("How much do you think you will spend on gas?"))
accomidation = int(input("Approximately, how much will you need for accomidations/hotel?"))
food = int(input("Last, how much will you need for food?"))
rem_bal = budget - fule - accomidation - food 
print("------------Travel Expenses------------")
print("Location:", location)
print("Initial Budget:", budget)

print("Fule:", fule)
print("Accomidations:", accomidation)
print("Food:", food ) 
print("Remaning Balance:", rem_bal)