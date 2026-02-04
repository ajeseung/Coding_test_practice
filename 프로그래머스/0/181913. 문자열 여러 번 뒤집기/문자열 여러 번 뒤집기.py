def solution(my_string, queries):
    arr = list(my_string)   # 문자열 → 리스트로 변환

    for s, e in queries:
        # s~e 구간 뒤집기
        arr[s:e+1] = arr[s:e+1][::-1]

    return "".join(arr)
