def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    vis = [[-1] * m for _ in range(n)]
    
    x = [-1, 0, 1, 0]
    y = [0, 1, 0, -1]
    
    Q = [[0,0]]
    vis[0][0] = 1
    while(Q):
        currX, currY = Q.pop(0)
        for i in range(4):
            nx = currX + x[i]
            ny = currY + y[i]
            
            # 범위를 벗어난 경우
            if(nx<0 or nx>=n or ny<0 or ny>=m):
                continue
            # 이미 방문한 경우
            if(vis[nx][ny] != -1):
                continue
            # 벽인 경우
            if(maps[nx][ny] == 0):
                continue
            
            vis[nx][ny] = vis[currX][currY] + 1
            Q.append([nx, ny])
    
    
    return vis[n-1][m-1]