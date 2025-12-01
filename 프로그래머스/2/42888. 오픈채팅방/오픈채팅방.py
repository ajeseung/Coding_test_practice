def solution(record):
    nickname = {}
    
    events = []
    
    for rec in record:
        parts = rec.split()
        action = parts[0]
        uid = parts[1]
        
        if action == "Enter":
            name = parts[2]
            nickname[uid] = name
            events.append((action, uid))
        elif action == "Leave":
            events.append((action, uid))
        elif action == "Change":
            name = parts[2]
            nickname[uid] = name
            
    
    answer = []
    for action, uid in events:
        name = nickname[uid]
        if action == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{name}님이 나갔습니다.")
            
    return answer