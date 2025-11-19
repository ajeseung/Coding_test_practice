def solution(numbers, hand):
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    left_pos = pos['*']
    right_pos = pos['#']
    answer = []

    for num in numbers:
        if num in [1, 4, 7]:
            answer.append('L')
            left_pos = pos[num]
        elif num in [3, 6, 9]:
            answer.append('R')
            right_pos = pos[num]
        else:  # 2, 5, 8, 0
            target = pos[num]
            left_dist = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
            right_dist = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])

            if left_dist < right_dist:
                answer.append('L')
                left_pos = target
            elif right_dist < left_dist:
                answer.append('R')
                right_pos = target
            else:  # 같은 거리면 hand
                if hand == "left":
                    answer.append('L')
                    left_pos = target
                else:
                    answer.append('R')
                    right_pos = target

    return "".join(answer)
