print('Celsius\tFahrenheit')

for c_temp in range(21):
    f_temp = 1.8 * c_temp + 32
    print(c_temp, format(f_temp, '.1f'), sep='\t')
