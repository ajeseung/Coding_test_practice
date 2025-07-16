# A, B, C를 입력받아 정수로 변환
A, B, C = map(int, input().split())

# 네 가지 값 계산 및 출력
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)