a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b ** 2 - (4 * a * c)
x1 = (-b - d ** 0.5) / (2 * a)
x2 = (-b + d ** 0.5) / (2 * a)
print(" 답은: ", x1, "and", x2)