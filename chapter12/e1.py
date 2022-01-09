def print_1_through_n(n):
    if n == 1:
        print(1)
        return

    print_1_through_n(n-1)
    print(n)

print_1_through_n(1)
print()
print_1_through_n(2)
print()
print_1_through_n(7)
