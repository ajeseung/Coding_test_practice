def solution(n, m):
    # 최대공약수 (유클리드 호제법)
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # 최소공배수는 두 수의 곱을 최대공약수로 나눈 값
    g = gcd(n, m)
    lcm = (n * m) // g

    return [g, lcm]
