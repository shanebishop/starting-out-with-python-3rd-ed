'''
Write a program that converts Celcius temperatures to
Farenheit temperatures. The formula is as follows:

  F = 9/5C + 32

The program should ask the user to enter a temperature
in Celcius, and then display the termperature
converted to Farenheit.
'''

c_temp = float(input('Enter temperature in Celcius: '))

# Dividing 9 by 5 may give an inaccurate result, so
# hardcode the decimal value of the fraction 9/5 for
# improved accuracy
f_temp = 1.8 * c_temp + 32

print('Temperature in Farenheit:', f_temp)
