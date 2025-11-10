import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Set<String> used = new HashSet<>();
        used.add(words[0]);

        for (int i = 1; i < words.length; i++) {
            String prev = words[i - 1];
            String cur  = words[i];

            boolean chainOk = prev.charAt(prev.length() - 1) == cur.charAt(0);
            boolean dupOk   = !used.contains(cur);

            if (!chainOk || !dupOk) {
                int player = i % n + 1;
                int turn   = i / n + 1;
                return new int[]{player, turn};
            }
            used.add(cur);
        }
        return new int[]{0, 0}; // 탈락자 없음
    }
}
