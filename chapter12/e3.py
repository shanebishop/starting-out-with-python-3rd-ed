def print_stars(n):
    if n == 1:
        print('*')
        return
    elif n < 1:
        return

    print_stars(n-1)
    print('*' * n)

print_stars(5)
print()
print_stars(1)
print_stars(0)
