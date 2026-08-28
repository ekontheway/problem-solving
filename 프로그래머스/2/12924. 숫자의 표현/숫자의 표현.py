def solution(n):
    answer = 0
    for i in range(1, n+1, 1):
        x = ((2*n)-(i-1)*i)/(2*i)
        if(x > 0 and x == int(x)):
            answer += 1
    return answer