t = int(input())

for i in range(t):
    a, b = input().split()
    a, b = int(a), int(b)

    print("Case #" + str(i + 1) + ":", a + b)