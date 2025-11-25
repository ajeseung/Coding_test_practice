a ,b = input().split()

reva = int(a[::-1])
revb = int(b[::-1])

print(max(reva, revb))