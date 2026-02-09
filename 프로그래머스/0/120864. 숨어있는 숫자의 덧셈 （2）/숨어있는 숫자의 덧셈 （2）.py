def solution(my_string):
    temp = ""
    result = 0

    for ch in my_string:
        if ch.isdigit():
            temp += ch
        else:
            if temp:
                result += int(temp)
                temp = ""

    # 마지막에 숫자로 끝났을 경우 처리
    if temp:
        result += int(temp)

    return result