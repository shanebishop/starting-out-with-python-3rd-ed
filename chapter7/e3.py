rainfalls = []

for month in range(1, 13):
    print('Enter rainfall for month ', month, ': ', sep='', end='')
    rainfall = float(input())
    rainfalls.append(rainfall)

total = sum(rainfalls)
average = total / 12

# Since indices are 0-based, add 1 to index to get
# the month
month_with_min = 1 + rainfalls.index(min(rainfalls))
month_with_max = 1 + rainfalls.index(max(rainfalls))

print()
print('Total rainfall:', total)
print('Average rainfall:', format(average, '.2f'))
print('Month with least rainfall:', month_with_min)
print('Month with most rainfall:', month_with_max)
