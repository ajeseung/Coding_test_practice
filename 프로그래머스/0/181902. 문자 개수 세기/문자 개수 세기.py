def solution(my_string):
    cnt = [0] * 52

    for ch in my_string:
        if 'A' <= ch <= 'Z':
            cnt[ord(ch) - ord('A')] += 1
        else:  # 'a' <= ch <= 'z'
            cnt[26 + (ord(ch) - ord('a'))] += 1

    return cnt
