from collections import Counter, deque

def is_valid(brackets):
    pair = {')':'(', '}' : '{', ']' : '['}
    stack = []
    
    for ch in brackets:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
    return not stack

def solution(s):
    n = len(s)
    if n % 2 == 1:
        return 0
    
    c = Counter(s)
    if c['('] != c[')'] or c['['] != c[']'] or c['{'] != c['}']:
        return 0
    
    d = deque(s)
    ans = 0
    for _ in range(n):
        if is_valid(''.join(d)):
            ans += 1
        d.append(d.popleft())
        
    return ans