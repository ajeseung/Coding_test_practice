T = int(input())

for _ in range(T):
    a, b = input().split()
    int_a = int(a)

    result = ""
    for i in range(len(b)):
        result += b[i] * int_a

    print(result)