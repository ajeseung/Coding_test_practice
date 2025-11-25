s = input().upper()

counts = [0] * 26

for ch in s:
    counts[ord(ch) - ord('A')] += 1

max_count = max(counts)

# max_count가 몇 번 등장했는지 확인
if counts.count(max_count) > 1:
    print("?")
else:
    print(chr(counts.index(max_count) + ord('A')))
