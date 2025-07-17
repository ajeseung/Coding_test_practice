def solution(phone_book):
    phone_set = set(phone_book)  # 1. 모든 번호를 set에 저장

    for number in phone_book:
        # 2. 접두어를 1자리부터 끝-1자리까지 잘라가며 확인
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in phone_set:
                return False  # 접두어가 실제 다른 번호로 존재하면 False

    return True  # 접두어가 없으면 True
