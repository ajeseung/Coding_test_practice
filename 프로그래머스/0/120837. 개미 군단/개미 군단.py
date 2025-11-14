def solution(hp):
    gen = hp//5
    sol = (hp - gen*5) // 3
    ordi = hp - (gen * 5) - (sol*3)
    
    return gen+sol+ordi
    
    