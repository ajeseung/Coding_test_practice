s = input()

# a~z 각각의 첫 등장 위치, 초기값은 전부 -1
positions = [-1] * 26

for idx, ch in enumerate(s):
    alpha_index = ord(ch) - ord('a')
    if positions[alpha_index] == -1:
        positions[alpha_index] = idx

print(*positions)
