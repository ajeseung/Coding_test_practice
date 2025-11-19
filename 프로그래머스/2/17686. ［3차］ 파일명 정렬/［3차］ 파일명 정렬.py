import re

def solution(files):
    parsed = []
    
    for file in files:
        head = ""
        number = ""
        tail_index = 0
        
        i = 0
        
        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1
            
        while i < len(file) and file[i].isdigit() and len(number) < 5:
            number += file[i]
            i += 1
            
        parsed.append((head, number, file))
        

    # 정렬 KEY:
    # 1) head.lower()
    # 2) int(number)
    # 파이썬 sort()는 stable-sort라 3순위 자동 처리됨
    parsed.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    # 원래 파일명만 반환
    return [x[2] for x in parsed]