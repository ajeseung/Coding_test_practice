def solution(arr, queries):
    def swap(a, i, j):
        a[i], a[j] = a[j], a[i]
    
    for i, j in queries:
        swap(arr, i, j)
    
    return arr
