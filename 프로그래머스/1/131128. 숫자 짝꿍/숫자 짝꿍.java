import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        int[] cntX = new int[10];
        int[] cntY = new int[10];
        
        for (int i = 0, n = X.length(); i < n; i++) {
            cntX[X.charAt(i) - '0']++;
        }
        for (int i = 0, n = Y.length(); i < n; i++) {
            cntY[Y.charAt(i) - '0']++;
        }
        
        System.out.println(Arrays.toString(cntX));
        System.out.println(Arrays.toString(cntY));
        int total = 0;
        
        for (int j =0; j <= 9; j++) total += Math.min(cntX[j], cntY[j]);
        if (total == 0) return "-1";

        StringBuilder sb = new StringBuilder(total);
        // 큰 숫자부터 붙이기
        for (int d = 9; d >= 0; d--) {
            int k = Math.min(cntX[d], cntY[d]);
            while (k-- > 0) sb.append((char) ('0' + d));
        }

        // 전부 0으로만 구성된 경우 → "0"
        if (sb.charAt(0) == '0') return "0";
        return sb.toString();
        
    }
}