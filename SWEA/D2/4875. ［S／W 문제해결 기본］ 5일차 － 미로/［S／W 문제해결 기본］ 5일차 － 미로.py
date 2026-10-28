from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]
    answer = 0
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                st = [i, j]
            elif board[i][j] == 3:
                en = [i, j]
                
    Q = deque([st])
    vis = [[0 for _ in range(N)] for _ in range(N)]
    vis[st[0]][st[1]] = 1
    dir = [[-1,0], [0,1],[1,0],[0,-1]]
    
    while(Q):
        currX, currY = Q.popleft()
        
        # 출발점=도착지
        if(currX == en[0] and currY== en[1]):
            answer = 1
            break
            
        if(board[currX][currY] == 1):
            continue
        
        for d in dir:
            nx = currX + d[0]
            ny = currY + d[1]
            
            if(nx==en[0] and ny==en[1]):
                answer = 1
                Q.clear()
                break
            
            if(nx<0 or nx>=N or ny<0 or ny>=N):
                continue
            
            if(vis[nx][ny] or board[nx][ny]==1):
                continue
                
            Q.append([nx, ny])
            vis[nx][ny] = 1
         
    print(f'#{test_case} {answer}')
