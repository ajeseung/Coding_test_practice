def solution(n, k):
    facto = [1] * (n+1)
    for i in range(1, n+1):
        facto[i] = facto[i-1] * i
    
    nums = list(range(1, n+1))
    k -= 1
    answer = []
    
    for l in range(n,0,-1):
        block_size = facto[l-1]
        idx = k // block_size
        k = k % block_size
        
        answer.append(nums[idx])
        nums.pop(idx)

    
    return answer