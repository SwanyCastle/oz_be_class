# 내가 푼 문제
def solution(n):
    for x in range(1, n):
        if n % x == 1:
            return x
        
# 다른 사람들이 푼 문제  - 굳이이렇게 까지해야하남 ,,,
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]
