def solution(s):
    words = s.split(" ")  # 공백 기준으로 단어 나누기
    result = []

    for word in words:
        converted = ''
        for i, ch in enumerate(word):
            if i % 2 == 0:
                converted += ch.upper()
            else:
                converted += ch.lower()
        result.append(converted)

    return ' '.join(result)