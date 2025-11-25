N = int(input())
scores = list(map(int, input().split()))

M = max(scores)

new_scores = [(s / M) * 100 for s in scores]
print(sum(new_scores) / N)
