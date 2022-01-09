age = int(input('Enter age:'))

if age <= 1:
    print('Infant')
elif age <= 13:
    print('Child')
elif age <= 20:
    print('Teenager')
elif age > 20:
    print('Adult')
else:
    print('Age must be nonnegative.')
