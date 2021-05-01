a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))
print("Favorite integers: ", a, b, c, d, e)
new_a = b + a + e
new_b = a + b + c
new_c = b + c + d
new_d = c + d + e 
new_e = d + e + a
a, b, c, d, e = new_a, new_b, new_c, new_d, new_e
print("Final integers: ", a, b, c, d, e)