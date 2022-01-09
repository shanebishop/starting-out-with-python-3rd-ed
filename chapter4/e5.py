years = int(input('Enter number of years: '))

sum = 0

for _ in range(years):
    for _ in range(12):  # 12 months per year
        sum += float(input('Enter rainfall in inches: '))

print('Total inches of rainfall:', sum)
print('Average rainfall per month:', sum / (years*12))
