def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

# Test cases
print(exactly_two_positive(2, 4, -3))  # True
print(exactly_two_positive(-4, 6, 8))  # True
print(exactly_two_positive(4, -6, 9))  # True
print(exactly_two_positive(-4, 6, 0))  # False
print(exactly_two_positive(4, 6, 10))  # False
print(exactly_two_positive(-14, -3, -4))  # False
