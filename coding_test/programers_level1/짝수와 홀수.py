# 내가 푼 문제
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

# 다른사람이 푼 문제 - 
def solution(num):
    return num % 2 and "Odd" or "Even"