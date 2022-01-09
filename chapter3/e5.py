mass = float(input('Enter mass in kg:'))

# https://en.wikipedia.org/wiki/Standard_gravity
weight = mass * 9.80665

if weight > 500:
    print('Too heavy')
elif weight < 100:
    print('Too light')
