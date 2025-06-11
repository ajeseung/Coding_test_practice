def convert(num, base):
    chars = "0123456789ABCDEF"
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        num, remainder = divmod(num, base)
        result = chars[remainder] + result
    return result

def solution(n, t, m, p):
    answer = ''
    full = ''
    num = 0

    # 필요한 길이까지 full 문자열 생성
    while len(full) < t * m:
        full += convert(num, n)
        num += 1

    # 튜브(p)의 차례에 해당하는 문자만 골라내기
    for i in range(t):
        answer += full[i * m + (p - 1)]

    return answer
