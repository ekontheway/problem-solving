T = int(input())
for test_case in range(1, T + 1):
    x, y, N = map(int, input().strip().split())
    answer = 0

    while(x<=N and y <=N):
        if(x>y):
            y += x
        else:
            x += y
        answer += 1
        
    print(answer)