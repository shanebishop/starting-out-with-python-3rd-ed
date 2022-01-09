pennies = int(input('Enter pennies: '))
nickels = int(input('Enter nickels: '))
dimes = int(input('Enter dimes: '))
quarters = int(input('Enter quarters: '))

total = pennies + nickels*5 + dimes*10 + quarters*25

if total == 100:
    print('Congratulations! Your entry adds to exactly a dollar.')
elif total < 100:
    print('Your entry is less than a dollar.')
else:
    print('Your entry is more than a dollar.')
