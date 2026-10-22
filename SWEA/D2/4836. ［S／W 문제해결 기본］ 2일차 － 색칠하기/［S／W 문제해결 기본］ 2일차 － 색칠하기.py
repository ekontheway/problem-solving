T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [[0] * 10 for _ in range(10 )]
    answer = 0
    for _ in range(N):
        arr = list(map(int, input().strip().split()))
        x1, y1, x2, y2, color = arr

        for row in range(x1, x2+1):
            for col in range(y1, y2+1):
                target = board[row][col]
                if(target == 0):
                    board[row][col] += color
                elif((target == 1 and color == 2) or ((target == 2 and color == 1))):
                    board[row][col] = 3
                    answer += 1
        
    print(f'#{test_case} {answer}')
        
        
        