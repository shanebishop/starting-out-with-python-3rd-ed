month = int(input('Enter month:'))
day = int(input('Enter day of month:'))
year = int(input('Enter year:'))

if month * day == year:
    print('The date is magic.')
else:
    print('The date is not magic.')
