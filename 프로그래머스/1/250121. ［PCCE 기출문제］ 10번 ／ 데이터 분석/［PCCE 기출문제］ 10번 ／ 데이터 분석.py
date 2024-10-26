def solution(data, ext, val_ext, sort_by):
    # 각 열의 인덱스를 매핑
    column_mapping = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    # 필터링 조건에 맞는 데이터 선택
    filtered_data = [row for row in data if row[column_mapping[ext]] < val_ext]

    # sort_by 기준으로 데이터 정렬
    sorted_data = sorted(filtered_data, key=lambda x: x[column_mapping[sort_by]])

    return sorted_data