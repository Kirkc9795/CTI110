#Christopher Kirk
#03/08/2025
#P2LAB2
#I am making a dictionary 

car_data = {
     "Camaro" : 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26 }

keys = car_data.keys()

print("Available Vehicles:", keys)
car = input("Enter a vehicle to see it's mpg:")
print(f"The {car} gets {car_data[car]} mpg")

miles = float(input(f"How many miles will you drive the {car} ? "))
mpg = car_data[car]
gallons_need = miles/mpg

print(f"{gallons_need:.2f} gallon(s) of gas are needed to drive {car} {miles} ")
