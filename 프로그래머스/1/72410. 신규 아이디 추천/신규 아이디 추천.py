def solution(new_id):
    s = new_id.lower()
    
    allowed = set('abcdefghijklmnopqrstuvwxyz0123456789-_.')
    s = ''.join(ch for ch in s if ch in allowed)
    
    while '..' in s:
        s = s.replace('..', '.')
    
    s = s.strip('.')
    
    if not s:
        s = 'a'
        
    if len(s) >= 16:
        s = s[:15]
        s = s.rstrip('.')
    
    while len(s) < 3:
        s += s[-1]
        
    return s