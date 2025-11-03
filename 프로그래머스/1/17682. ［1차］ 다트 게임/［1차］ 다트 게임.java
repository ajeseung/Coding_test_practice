class Solution {
    public int solution(String dartResult) {
        int[] scores = new int[3];
        int round = -1;
        int n = dartResult.length();
        
        for(int i=0; i < n; i++) {
            char ch = dartResult.charAt(i);
            
            if(Character.isDigit(ch)) {
                round++;
                int val = ch -'0';
                
                if(ch == '1' && i+1 < n && dartResult.charAt(i+1) == '0') {
                    val = 10;
                    i++;
                }
                scores[round] = val;
            }
            
            else if(ch == 'S' || ch == 'D' || ch == 'T') {
                int v = scores[round];
                
                switch(ch) {
                    case 'S':
                        scores[round] = (int) Math.pow(v,1);
                        break;
                    case 'D':
                        scores[round] = (int) Math.pow(v,2);
                        break;
                    case 'T':
                        scores[round] = (int) Math.pow(v,3);
                        break;                        
                }
                
                if(i+1 < n) {
                    char next = dartResult.charAt(i+1);
                    if (next == '*') {
                        scores[round] *= 2;
                        if (round - 1 >= 0) {
                            scores[round -1] *= 2;
                        }
                        i++;
                    } else if (next == '#') {
                        scores[round] *= -1;
                        i++;
                    }
                }
            }
        }
        
        return scores[0] + scores[1] + scores[2];
    }
}