def least(a, b, c):
    if a <= b <= c or a <= c <= b:
        return a
    if b <= a <= c or b <= c <= a:
        return b
    return c


print(least(1, 2, 3))
print(least(2, 1, 3))
print(least(1, 1, 3))