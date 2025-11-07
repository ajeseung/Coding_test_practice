class Solution {
    public int solution(int[] ingredient) {
        // ingredient[i] ∈ {1(빵), 2(야채), 3(고기)}
        int n = ingredient.length;
        int[] stack = new int[n]; // 스택 역할
        int top = 0;              // 스택 크기(다음 push 위치)
        int burgers = 0;

        for (int x : ingredient) {
            stack[top++] = x;

            // 스택에 최소 4개 쌓였고, 상단 4개가 1-2-3-1이면 포장
            if (top >= 4 &&
                stack[top - 4] == 1 &&
                stack[top - 3] == 2 &&
                stack[top - 2] == 3 &&
                stack[top - 1] == 1) {
                top -= 4;   // 4개 pop
                burgers++;  // 햄버거 1개 완성
            }
        }
        return burgers;
    }
}
