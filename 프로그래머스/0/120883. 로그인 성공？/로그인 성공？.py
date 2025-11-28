def solution(id_pw, db):
    for i in range(len(db)):
        db_arr = db[i]
        # 아이디가 같은지 먼저 확인
        if id_pw[0] == db_arr[0]:
            if id_pw[1] == db_arr[1]:
                return "login"
            else:
                return "wrong pw"
    # 여기까지 왔다는 건 아이디가 한 번도 안 나온 것
    return "fail"
