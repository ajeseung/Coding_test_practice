from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (초기에는 빈 다리)
    bridge_weight = 0  # 현재 다리 위의 총 무게
    truck_weights = deque(truck_weights)  # 트럭 대기 큐
    
    while truck_weights or bridge_weight > 0:
        time += 1
        
        # 다리의 맨 앞 트럭이 다리를 다 건넜는지 확인 (한 칸 이동)
        bridge_weight -= bridge.popleft()
        
        # 새로운 트럭을 다리에 올릴 수 있는지 확인
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                # 새로운 트럭이 다리에 올라갈 수 있으면 올림
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                # 다리의 무게를 초과하면 빈칸(0)을 다리에 올림
                bridge.append(0)
    
    return time
