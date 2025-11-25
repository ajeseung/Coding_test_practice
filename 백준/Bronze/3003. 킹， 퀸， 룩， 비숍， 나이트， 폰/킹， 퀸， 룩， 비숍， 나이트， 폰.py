ordi = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))

result = []

for o,f in zip(ordi, found):
    result.append(o-f)
    
print(*result)