DAYS = 5

sum = 0

for day in range(1, DAYS+1):
    print('How many bugs collected on day ', day, '? ', sep='', end='')
    sum += int(input())

print('Total number of bugs collected:', sum)
