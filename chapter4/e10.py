tuition = 8000
years = 5

for year in range(1, years+1):
    tuition *= 1.03
    print(year, format(tuition, '.2f'), sep='\t')
