class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 0;
        
        while(a != b) {
            int updated_a = (a + 1) / 2;
            int updated_b = (b + 1) / 2;
            
            a = updated_a;
            b = updated_b;
            
            answer++;
            
        }

        return answer;
    }
}