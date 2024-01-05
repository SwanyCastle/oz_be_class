# 내가푼 문제
def solution(arr):
    answer = []
    
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(int(i / 2))
        elif i < 50 and i % 2 == 1:
            answer.append(i * 2)
        else:
            answer.append(i)
    
    return answer

# int(a/b)와 a//b의 차이는 a//b는 나눈 값을 내림처리를 진행하지만, int()는 소수점을 버리는 처리의 차이가 존재합니다.

# int(-1 / 2) => int(-0.5) => 0

# -1 // 2 => -1