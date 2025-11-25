submitted = set()

for _ in range(28):
    submitted.add(int(input()))

# 전체 번호 집합
all_students = set(range(1, 31))

# 제출 안 한 학생들
not_submitted = sorted(all_students - submitted)

print(not_submitted[0])
print(not_submitted[1])
