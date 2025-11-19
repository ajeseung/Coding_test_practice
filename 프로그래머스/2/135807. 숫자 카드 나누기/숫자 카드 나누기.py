from math import gcd

def solution(arrayA, arrayB):
    def get_gcd(arr):
        g = arr[0]
        for x in arr[1:]:
            g = gcd(g,x)
        return g
    
    gcd_A = get_gcd(arrayA)
    gcd_B = get_gcd(arrayB)
    
    def valid(g, other):
        for x in other:
            if x % g == 0:
                return 0
        return g
            
    candidate1 = valid(gcd_A, arrayB)
    candidate2 = valid(gcd_B, arrayA)
    
    return max(candidate1, candidate2)