numbers = []

for _ in range(9):
    numbers.append(int(input()))

max_value = max(numbers)          # 최댓값
max_index = numbers.index(max_value) + 1   # 0부터 시작하므로 +1

print(max_value)
print(max_index)
