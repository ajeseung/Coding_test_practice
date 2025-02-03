def solution(diffs, times, limit):
    def can_complete(level):
        total_time = 0
        prev_time = 0

        for diff, time_cur in zip(diffs, times):
            if diff <= level:
                total_time += time_cur
            else:
                mistakes = diff - level
                total_time += mistakes * (time_cur + prev_time) + time_cur

            if total_time > limit:
                return False

            prev_time = time_cur

        return total_time <= limit

    left, right = 1, max(diffs)
    while left < right:
        mid = (left + right) // 2
        if can_complete(mid):
            right = mid
        else:
            left = mid + 1

    return left