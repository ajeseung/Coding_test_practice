import heapq

def solution(jobs):
    # 요청 시간으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    # 현재 시간
    time = 0
    # 완료된 작업의 개수
    count = 0
    # 총 소요 시간 (작업의 요청부터 종료까지의 누적 시간)
    total_time = 0
    # 작업 대기 목록 (최소 힙)
    heap = []
    # jobs의 인덱스
    job_index = 0
    n = len(jobs)
    
    # 작업이 남아 있을 때까지 처리
    while count < n:
        # 현재 시간까지 도착한 작업들을 힙에 추가
        while job_index < n and jobs[job_index][0] <= time:
            heapq.heappush(heap, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        
        if heap:
            # 소요 시간이 가장 짧은 작업을 선택
            job_duration, job_start = heapq.heappop(heap)
            # 현재 시각을 갱신 (작업 수행)
            time += job_duration
            # 해당 작업의 요청부터 종료까지의 소요 시간을 누적
            total_time += time - job_start
            count += 1
        else:
            # 처리할 작업이 없으면 다음 작업이 요청되는 시간으로 이동
            time = jobs[job_index][0]
    
    # 평균 소요 시간을 반환 (소수점 이하 버림)
    return total_time // n
