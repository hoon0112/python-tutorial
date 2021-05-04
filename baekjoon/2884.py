def alarm(h, m):
    if m >= 45:
        m -= 45
    else:
        if h > 0:
            h -= 1
        else:
            h = 23
        m += 15
    return (h, m)

h, m = map(int, input().split())
seth, setm = alarm(h, m) # unpacking
print(seth, setm)