def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def solution(arr):
    answer = lcm(arr[0], arr[1])
    cnt = 2
    while(cnt < len(arr)):
        answer = lcm(answer, arr[cnt])
        cnt += 1        

    return answer