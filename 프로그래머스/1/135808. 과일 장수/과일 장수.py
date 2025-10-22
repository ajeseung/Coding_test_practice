def solution(k, m, score):
    score.sort(reverse=True)      # 높은 점수부터
    total = 0
    # m개씩 끊어가며, 묶음의 마지막 값이 그 상자의 최소점수 p
    for i in range(m - 1, len(score), m):
        total += score[i] * m
    return total
