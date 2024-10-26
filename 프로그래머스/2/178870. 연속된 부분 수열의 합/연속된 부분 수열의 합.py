def solution(sequence, k):
    start, end = 0, 0
    min_length = float('inf')
    result = []

    current_sum = sequence[0]

    while start < len(sequence) and end < len(sequence):
        if current_sum == k:
            if end - start < min_length:
                min_length = end - start
                result = [start, end]

            current_sum -= sequence[start]
            start += 1
            if start > end:
                end = start
                if end < len(sequence):
                    current_sum = sequence[end]
        elif current_sum < k:
            end += 1
            if end < len(sequence):
                current_sum += sequence[end]
        else:
            current_sum -= sequence[start]
            start += 1
            if start > end:
                end = start
                if end < len(sequence):
                    current_sum = sequence[end]

    return result

# Test cases
print(solution([1, 2, 3, 4, 5], 7))  # [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5))  # [6, 6]
print(solution([2, 2, 2, 2, 2], 6))  # [0, 2]
