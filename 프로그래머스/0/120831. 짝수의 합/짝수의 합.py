def sum(num):
    cnt = 0
    for i in range(num+1):
        cnt += i
    return cnt

def solution(n):
    return 2*sum(n//2)