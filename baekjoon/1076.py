def str_to_num(s):
    if s == "black":
        return 0
    if s == "brown":
        return 1
    if s == "red":
        return 2
    if s == "orange":
        return 3
    if s == "yellow":
        return 4
    if s == "green":
        return 5
    if s == "blue":
        return 6
    if s == "violet":
        return 7
    if s == "grey":
        return 8
    if s == "white":
        return 9
    return -1

 
def prodval(x):
    return 10 ** x


a = str_to_num(input())
b = str_to_num(input())
c = str_to_num(input())

print((a * 10 + b) * prodval(c))