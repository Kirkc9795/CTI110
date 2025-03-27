#Christopher Kirk
#03/27/2025
#P3HW2
# Getting employees hours worked and pay rate 

name = input("Enter emoloyee's name:" )
hours_worked = float(input("Enter number of hours worked:"))
pay_rate = float(input("Enter employee's pay rate:"))
print('-------------------------------')

overtime_hours = 0
overtime_pay = 0 
reg_pay = 0

if hours_worked > 40:
    reg_hours = 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    reg_hours = hours_worked

reg_pay = reg_hours * pay_rate
gross_pay = reg_pay + overtime_pay
   
   
print(f"Employee's name: {name}\n")

print(f'Hours worked\t Pay Rate\t OverTime\t OverTime Pay\t RegHour Pay\t Gross Pay')
print('--------------------------------------------------------------------------------------------------')
print(f'{hours_worked}\t\t {pay_rate}\t\t {overtime_hours}\t\t {overtime_pay:.2f}\t\t ${reg_pay:.2f}\t ${gross_pay:.2f}')
