days = int(input('Enter days: '))

salary = 1

for day in range(1, days+1):
    print(day, '\t$', format(salary, '.2f'), sep='')
    salary *= 2
