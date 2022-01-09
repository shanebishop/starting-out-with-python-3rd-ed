def sum(l):
    if l == []:
        return 0

    return l[0] + sum(l[1:])

assert sum([]) == 0
assert sum([1]) == 1
assert sum([1,3,4,5]) == 13
