# 문자열 입력
# 문자열 내에 'p', 'y' 의 갯수가 같으면 true, 다르면 false (대소문자 구분없이)

# 내가 푼 답
def solution(s):
    answer = True
    c1 = 0
    c2 = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            c1 += 1
        elif i == 'y' or i == 'Y':
            c2 += 1
            
    if c1 is c2:
        answer = True
    else:
        answer = False    

    return answer

# 다른사람이 푼 답
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
# 와 이건 생각도 못했다 내껀 초딩수준ㅋㅋㅋㅋ