def solution(arr, flag):
    X = []

    for a, f in zip(arr, flag):
        if f:
            X.extend([a] * (a * 2))
        else:
            # 뒤에서 a개 제거
            X = X[:-a]

    return X
