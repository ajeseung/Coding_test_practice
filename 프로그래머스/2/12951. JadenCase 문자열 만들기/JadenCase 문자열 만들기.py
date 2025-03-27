def solution(s):
    words = s.split(' ')
    
    jaden_words = []
    for word in words:
        if word:
            jaden_word = word[0].upper()+ word[1:].lower()
        else:
            jaden_word = ''
        jaden_words.append(jaden_word)
        
    result = ' '.join(jaden_words)
    return result