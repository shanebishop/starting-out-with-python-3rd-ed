def pow(base, power):
    '''power must be an integer'''

    if power == 0:
        return 1
    if power == 1:
        return base

    # Handle negative powers
    # NOTE: This is bad if the base is 0 and
    # the power is negative
    if power < 0:
        power = -power
        base = 1/base

    return base * pow(base, power-1)

assert pow(3, 1) == 3
assert pow(3, 0) == 1
assert pow(3, 3) == 27
assert pow(4, -1) == 0.25
assert pow(2, -2) == 0.25
assert pow(-2, 3) == -8
assert pow(-2, 4) == 16
assert pow(-2, -2) == 0.25
assert pow(-2, 0) == 1
assert pow(-2, 1) == -2
assert pow(-4, -1) == -0.25
