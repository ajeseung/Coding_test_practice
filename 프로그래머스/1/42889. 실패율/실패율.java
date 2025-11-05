import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        // 1) 각 스테이지에 머문 사용자 수 집계 (N+1 포함)
        int[] stay = new int[N + 2]; // 인덱스: 1..N+1
        for (int s : stages) {
            if (1 <= s && s <= N + 1) stay[s]++;
        }

        // 2) 실패율 계산
        double[] fail = new double[N + 1]; // 인덱스: 1..N
        int reached = stages.length;       // 현재 스테이지에 "도달한" 사람 수
        for (int i = 1; i <= N; i++) {
            if (reached == 0) {
                fail[i] = 0.0;
            } else {
                fail[i] = (double) stay[i] / reached;
            }
            reached -= stay[i]; // 다음 스테이지에 도달한 사람 수로 갱신
        }

        // 3) 정렬: 실패율 내림차순, 동률이면 스테이지 번호 오름차순
        Integer[] order = new Integer[N];
        for (int i = 0; i < N; i++) order[i] = i + 1;

        Arrays.sort(order, (a, b) -> {
            int cmp = Double.compare(fail[b], fail[a]); // 내림차순
            if (cmp != 0) return cmp;
            return Integer.compare(a, b);               // 번호 오름차순
        });

        // 4) 결과 변환
        int[] answer = new int[N];
        for (int i = 0; i < N; i++) answer[i] = order[i];
        return answer;
    }
}
