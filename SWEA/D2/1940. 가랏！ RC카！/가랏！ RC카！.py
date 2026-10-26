T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    speed = 0
    distance = 0
    for _ in range(N):
        arr = list(map(int, input().strip().split())) + [0]
        cmd1 = arr[0]
        cmd2 = arr[1]
        
        # 가속
        if(cmd1 == 1):
            speed += cmd2
        # 감속
        elif(cmd1 == 2):
            speed -= cmd2
            if(speed < 0):
                speed = 0
        distance += speed
        
    print(f'#{test_case} {distance}')        