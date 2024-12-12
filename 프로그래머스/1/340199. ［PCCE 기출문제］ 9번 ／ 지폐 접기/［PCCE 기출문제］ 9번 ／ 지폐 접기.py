def solution(wallet, bill):
    wallet_width, wallet_height = sorted(wallet)
    bill_width, bill_height = sorted(bill)
    
    answer = 0
    
    while bill_width > wallet_width or bill_height > wallet_height:
        if bill_width > bill_height:
            bill_width//=2
        else:
            bill_height//=2
        answer+=1
        
        bill_width, bill_height = sorted([bill_width, bill_height])
        
    return answer