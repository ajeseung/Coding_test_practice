def solution(arr, delete_list):
    delete_set = set(delete_list)  # 탐색 O(1)
    return [x for x in arr if x not in delete_set]
