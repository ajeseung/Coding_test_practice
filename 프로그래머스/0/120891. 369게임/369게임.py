def solution(order):
    char = str(order)
    return char.count("3") + char.count("6") + char.count("9")
