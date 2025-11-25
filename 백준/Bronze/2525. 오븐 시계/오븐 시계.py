A, B = map(int, input().split())  # 현재 시각: 시, 분
C = int(input())                  # 걸리는 시간(분)

total = A * 60 + B + C            # 전부 '분'으로 환산해서 더하기

end_H = (total // 60) % 24        # 시: 60으로 나눈 몫, 24로 한 번 더 나머지
end_M = total % 60                # 분: 60으로 나눈 나머지

print(end_H, end_M)
