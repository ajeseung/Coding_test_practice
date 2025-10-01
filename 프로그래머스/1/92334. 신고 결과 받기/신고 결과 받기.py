def solution(id_list, report, k):
    report_set = set(report)
    
    reporters_of = {uid: set() for uid in id_list}   # 피신고자 -> (신고자들)
    reported_by_me = {uid: set() for uid in id_list} # 신고자 -> (내가 신고한 피신고자들)
    
    for item in report_set:
        reporter, target = item.split()
        reporters_of[target].add(reporter)
        reported_by_me[reporter].add(target)

    # 4) 정지 대상 산출
    banned = {uid for uid, reporters in reporters_of.items() if len(reporters) >= k}

    # 5) 메일 횟수 계산
    #    (내가 신고한 대상들 중 정지된 사람 수)
    answer = []
    for uid in id_list:
        cnt = sum(1 for target in reported_by_me[uid] if target in banned)
        answer.append(cnt)

    return answer