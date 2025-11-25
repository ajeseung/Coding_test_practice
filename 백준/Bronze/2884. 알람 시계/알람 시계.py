a, b = map(int, input().split())
    
if b >= 45:
    c = b-45
    print(a, c)
elif a != 0 and b < 45:
    d = 45 - b
    e = 60 - d
    f = a - 1
    print(f, e)
elif a == 0 and b < 45:
    g = 45 - b
    h = 60 - g
    print('23', h)