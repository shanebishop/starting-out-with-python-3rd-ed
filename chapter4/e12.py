start_num = int(input('Starting number of organisms: '))
daily_increase_percent = float(input('Average daily increase: '))
days = int(input('Number of days to multiply: '))

# Convert percent to number
daily_increase = daily_increase_percent / 100

pop = start_num

for day in range(1, days+1):
    print(day, format(pop, '.4f'), sep='\t')
    pop *= 1 + daily_increase
