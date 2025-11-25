N, X = map(int, input().split())
arr = list(map(int, input().split()))

answer = ""

for value in arr:
    if value < X:
        answer += str(value) + " "

print(answer.strip())
