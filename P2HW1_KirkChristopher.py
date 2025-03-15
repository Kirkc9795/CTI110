# Christopher Kirk
# 03/15/2025
# P2HW1
# This project is on basic math on numbers that are entered usining float numbers
print("This program calculates and displays travel expenses" )
budget = float(int(input("Enter budget:")))
location = input("Enter your travel destination:")
fule = float(int(input("How much do you think you will spend on gas?")))
accomidation = float(int(input("Approximately, how much will you need for accomidations/hotel?")))
food = float(int(input("Last, how much will you need for food?")))
rem_bal = budget - fule - accomidation - food 
print("------------Travel Expenses------------")
print(f"Location: \t\t{location}")
print(f"Budget: \t\t${budget:.2f}")

print(f"fule: \t\t\t${fule:.2f}")
print(f"Acocomidation: \t\t${accomidation:.2f}")
print(f"Food: \t\t\t${food:.2f}")

print("---------------------------------------")


print(f"Remaining Balance: \t${rem_bal:.2f}")