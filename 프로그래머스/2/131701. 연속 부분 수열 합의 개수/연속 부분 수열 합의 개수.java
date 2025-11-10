import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int n = elements.length;
        int[] doubleElements = new int[n * 2];
        
        // 1️⃣ 원형 처리를 위해 배열 2배로 확장
        for (int i = 0; i < n * 2; i++) {
            doubleElements[i] = elements[i % n];
        }

        // 2️⃣ 누적합(prefix sum) 계산
        int[] prefixSum = new int[n * 2 + 1];
        for (int i = 0; i < n * 2; i++) {
            prefixSum[i + 1] = prefixSum[i] + doubleElements[i];
        }

        // 3️⃣ 부분합을 저장할 Set (중복 제거)
        Set<Integer> sums = new HashSet<>();

        // 4️⃣ 길이 1~n까지 가능한 연속 부분 수열의 합 계산
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i < n; i++) {
                int sum = prefixSum[i + len] - prefixSum[i];
                sums.add(sum);
            }
        }

        // 5️⃣ 중복 제거된 합의 개수 반환
        return sums.size();
    }
}
