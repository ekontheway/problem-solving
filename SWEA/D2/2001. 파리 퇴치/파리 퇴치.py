T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    
    answer = 0
    
    for row in range(N-M+1):
        for col in range(N-M+1):
            total = 0
            for i in range(row, row+M):
                for j in range(col, col+M):
                    total += arr[i][j]
                
            answer = max(answer, total) 
            
    print(f'#{test_case} {answer}')