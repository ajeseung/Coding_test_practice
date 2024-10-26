#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// section_len은 배열 section의 길이입니다.
int solution(int n, int m, int section[], size_t section_len) {
    size_t index = 0;
    int paint_count = 0;
    
    while(index < section_len){
        int cover_end = section[index] + m - 1;
        while(index < section_len && section[index] <= cover_end){
            index++;
        }
        paint_count++;
    }
    return paint_count;
}