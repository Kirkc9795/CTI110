#Christopher Kirk 
#04/10/2025
#P4HW2
#Looping the employee name and hours worked calculator



name = "" 

total_employees = 0
total_overtime_pay = 0
total_reg_pay = 0
total_gross_pay = 0


name = input('Enter employee''s name or ''Done'' to terminate: ')  


while name != "done":
    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f'What is {name}''s pay rate? ' ))

   
    overtime_hours = hours_worked - 40
    reg_hours = hours_worked - overtime_hours
    reg_pay = reg_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = reg_pay + overtime_pay


    print(f'\nEmployee name:\t{name}')
    print(f'\n{'Hours Worked'}\t\t\t{'Pay Rate'}\t\t{'OverTime'}\t\t{'OverTime Pay'}\t\t\t{'RegHour Pay'}\t\t\t{'Gross Pay'}\t\t')
    print('--------------------------------------------------------------------------------------------------------------------------------')
    print(f'{hours_worked:.1f}\t\t\t\t{pay_rate:.2f}\t\t\t{overtime_hours:.1f}\t\t\t{overtime_pay:.2f}\t\t\t\t{reg_pay:.2f}\t\t\t\t${gross_pay:.2f}\t\t\t\n')

    total_employees += 1
    total_overtime_pay += overtime_pay
    total_reg_pay += reg_pay
    total_gross_pay += gross_pay
    name = input('Enter employee''s name or ''Done'' to terminate: ')  


print(f'\nTotal number of employees entered: {total_employees}')
print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
print(f'Total amount paid for reg hours: ${total_reg_pay:.2f}')
print(f'Total amount paid in gross: ${total_gross_pay:.2f}')
