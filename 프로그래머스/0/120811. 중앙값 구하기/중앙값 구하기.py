def solution(array):
    med = len(array) // 2
    
    array.sort()
    return array[med]