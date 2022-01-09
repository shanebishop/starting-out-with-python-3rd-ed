sum = 0

for year in range(1, 26):
    sum += 1.6
    print(year, format(sum, '.1f'), sep='\t')
