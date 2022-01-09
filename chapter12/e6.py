def sum(n):
    if n == 1:
        return 1

    return n + sum(n-1)

assert sum(1) == 1
assert sum(2) == 3
assert sum(5) == 5 + 4 + 3 + 2 + 1
