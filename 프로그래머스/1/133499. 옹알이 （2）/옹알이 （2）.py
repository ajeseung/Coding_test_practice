def solution(babbling):
    syllables = ["aya", "ye", "woo", "ma"]
    count = 0

    for bab in babbling:
        i = 0
        prev = None
        ok = True

        while i < len(bab):
            matched = False
            for s in syllables:
                if s != prev and bab.startswith(s, i):
                    i += len(s)
                    prev = s
                    matched = True
                    break
            if not matched:
                ok = False
                break

        if ok and i == len(bab):
            count += 1

    return count
