#Christopher Kirk
#04/04/2025
#P4LAB2
#Making a program that multiplies using while loops and  using for loops 


again = 'yes'

while again != 'no':

    num = int(input('Enter an integer: '))

    if num >= 0:
        for item in range(1,13):
            print(f'{num} * {item} = {num * item}')
    else:
        print('This program does not handel negative numbers.')
    
    again = input('Would you like to run the program again? ')

print('Exiting program  . . . ')