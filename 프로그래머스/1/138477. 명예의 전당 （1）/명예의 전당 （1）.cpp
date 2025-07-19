#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> answer;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    for (int i = 0; i < score.size(); ++i) {
        if (minHeap.size() < k) {
            minHeap.push(score[i]);
        } else {
            if (score[i] > minHeap.top()) {
                minHeap.pop();
                minHeap.push(score[i]);
            }
        }
        answer.push_back(minHeap.top());
    }

    return answer;
}