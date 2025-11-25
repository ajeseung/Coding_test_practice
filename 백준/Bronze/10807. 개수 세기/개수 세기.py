N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

count = 0
for num in numbers:
    if num == v:
        count += 1

print(count)
