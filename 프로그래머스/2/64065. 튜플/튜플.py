def solution(s):
    inside = s[2:-2]
    
    parts = inside.split("},{")
    
    sets = []
    
    for part in parts:
        nums = list(map(int, part.split(',')))
        sets.append(nums)
        
    sets.sort(key = len)
    
    result = []
    
    seen = set()
    
    for arr in sets:
        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)
                break
                
    return result