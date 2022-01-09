num = int(input('Enter positive nonzero number: '))

if num <= 0:
    print('Entered number is not a positive nonzero number.')
    exit()

prod = 1

for multiplicand in range(1, num+1):
    prod *= multiplicand

print(num, '! = ', prod, sep='')
