import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> temp = new HashMap<>();
        for (int size: tangerine) {
            temp.put(size, temp.getOrDefault(size,0) + 1);
        }
        
        List<Integer> counts = new ArrayList<>(temp.values());

        counts.sort(Collections.reverseOrder());

        int usedTypes = 0;
        int taken = 0;
        for (int c : counts) {
            taken += c;
            usedTypes++;
            if (taken >= k) break;
        }
        return usedTypes;
    }
}