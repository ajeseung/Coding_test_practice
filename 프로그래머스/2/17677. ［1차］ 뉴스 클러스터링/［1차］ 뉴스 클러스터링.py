from collections import Counter

def to_bigrams(s: str):
    s = s.lower()
    out = []
    for i in range(len(s) - 1):
        a, b = s[i], s[i+1]
        if 'a' <= a <= 'z' and 'a' <= b <= 'z':
            out.append(a + b)
    return out

def solution(str1: str, str2: str) -> int:
    c1 = Counter(to_bigrams(str1))
    c2 = Counter(to_bigrams(str2))

    if not c1 and not c2:
        return 65536

    inter = c1 & c2
    union = c1 | c2

    inter_size = sum(inter.values())
    union_size = sum(union.values())

    jaccard = inter_size / union_size
    return int(jaccard * 65536)
