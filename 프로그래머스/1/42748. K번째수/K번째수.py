def solution(array, commands):
    result = []
    
    # commands의 각 명령을 처리
    for command in commands:
        i, j, k = command
        # i번째부터 j번째까지 자르고 정렬한 후 k번째 숫자 추출
        sliced_array = sorted(array[i-1:j])
        result.append(sliced_array[k-1])
    
    return result
