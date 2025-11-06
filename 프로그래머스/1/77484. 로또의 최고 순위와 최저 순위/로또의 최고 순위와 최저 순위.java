import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        Arrays.sort(lottos);
        Arrays.sort(win_nums);
        
        int i = 0;
        int zeros = 0;
        
        while (i<6 && lottos[i] == 0) {
            i++;
            zeros++;
        }
        
        int j = 0;
        int hits = 0;
        
        while(i<6 && j<6) {
            if (lottos[i] == win_nums[j]) {
                hits++;
                i++;
                j++;
            } else if (lottos[i] < win_nums[j]) {
                i++;
            } else {
                j++;
            }
        }
        
        int best = hits + zeros;
        int worst = hits;
        
        return new int[]{ toRank(best), toRank(worst) };
    }
    
    private int toRank(int matches) {
        int rank = 7-matches;
        
        if (rank < 1) return 1;
        if (rank > 6) return 6;
        
        return rank;
    }
}