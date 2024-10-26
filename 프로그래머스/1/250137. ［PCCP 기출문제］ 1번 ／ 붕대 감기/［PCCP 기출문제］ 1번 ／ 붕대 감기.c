#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// bandage_len은 배열 bandage의 길이입니다.
// attacks_rows는 2차원 배열 attacks의 행 길이, attacks_cols는 2차원 배열 attacks의 열 길이입니다.
int solution(int bandage[], size_t bandage_len, int health, int** attacks, size_t attacks_rows, size_t attacks_cols) {
    int t = bandage[0], x = bandage[1], y = bandage[2];
    
    int current_health = health, continuous_success = 0;
    
    //마지막 공격시간
    int last_attack_time = attacks[attacks_rows - 1 ][0];
    
    for(int time = 0; time <= last_attack_time; time++){
        int attacked = 0;
        
        //현재 시간에 공격이 있는지 판단
        for (int i =0; i < attacks_rows; i++){
            if(attacks[i][0] == time){
                current_health -= attacks[i][1];
                if(current_health <= 0){
                    return -1;
                }
                continuous_success = 0;
                attacked = 1;
                break;
            }
        }
        if(!attacked){
            //붕대감기 성공
            if(continuous_success < t){
                current_health += x;
                if(current_health > health){
                    current_health = health;
                }
                continuous_success++;
            }
            //연속성공 시간이 t에 도달한다면
            if(continuous_success == t){
                current_health += y;
                if(current_health > health){
                    current_health = health;
                }
                continuous_success = 0;
            }
        }
    }
    return current_health;
}

