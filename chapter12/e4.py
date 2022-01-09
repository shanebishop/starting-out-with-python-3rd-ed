def largest(l):
    if len(l) == 1:
        return l[0]

    first = l[0]
    largest_rest = largest(l[1:])
    return first if first > largest_rest else largest_rest

assert largest([1,2]) == 2
assert largest([1]) == 1
assert largest([2,1]) == 2
assert largest([3,1,2]) == 3
assert largest([2,1,3]) == 3
assert largest([3,3]) == 3
