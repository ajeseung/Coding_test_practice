def solution(today, terms, privacies):
    def return_date_to_day(date_str):
        y, m, d = map(int, date_str.split('.'))
        return (y*12*28) + (m*28) + d
    
    today_days = return_date_to_day(today)
    
    term_dict = {}
    
    for term in terms:
        type_, months = term.split()
        term_dict[type_] = int(months)
        
    result = []
    for i, privacy in enumerate(privacies):
        date_str, term_type = privacy.split()
        collected_day = return_date_to_day(date_str)
        expire_day = collected_day + term_dict[term_type] * 28
        
        if expire_day <= today_days:
            result.append(i+1)
    
    return result