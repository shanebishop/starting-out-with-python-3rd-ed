sum = 0

while True:
    num = float(input('Enter number: '))

    if num < 0:
        break

    sum += num

print('Sum:', sum)
