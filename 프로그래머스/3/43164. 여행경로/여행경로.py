def solution(tickets):
    # 항공권을 출발지와 도착지 기준으로 알파벳 순서대로 정렬
    tickets.sort()

    # 경로를 담을 리스트
    answer = []
    
    # DFS 탐색을 위한 함수
    def dfs(airport, path):
        # 모든 티켓을 사용했을 경우 경로 완성
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return True
        
        # 모든 티켓을 순서대로 탐색
        for i, (src, dst) in enumerate(tickets):
            if src == airport:  # 현재 공항에서 출발하는 티켓이 있으면
                tickets[i] = ('', '')  # 사용한 티켓은 공백으로 표시
                if dfs(dst, path + [dst]):  # 다음 공항으로 이동
                    return True
                tickets[i] = (src, dst)  # 탐색 실패 시 티켓 원복

        return False

    # "ICN"에서 출발하여 경로 탐색 시작
    dfs("ICN", ["ICN"])
    
    return answer[0]  # 알파벳 순으로 정렬된 첫 번째 경로 반환
