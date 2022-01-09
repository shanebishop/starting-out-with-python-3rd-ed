def mult(x, y):
    '''x and y must both be integers'''

    # Ensure x is the smaller argument, to minimize
    # recursive calls
    if x > y:
        x, y = y, x

    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y

    # Ensure negative integers eventually hit the
    # base case, by making x always be nonnegative
    if x < 0:
        x = -x
        y = -y

    return y + mult(x-1, y)

assert mult(7, 4) == 28
assert mult(4, 7) == 28
assert mult(5, 5) == 25
assert mult(-5, 6) == -30
assert mult(-6, 5) == -30
assert mult(4, -3) == -12
assert mult(-4, 3) == -12
assert mult(-7, -2) == 14
assert mult(0, 2) == 0
assert mult(-5, 0) == 0
print('All assertions passed.')
