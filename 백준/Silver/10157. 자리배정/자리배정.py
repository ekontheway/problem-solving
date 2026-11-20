C, R = map(int, input().strip().split())
K = int(input())

board = [[0] * C for _ in range(R)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

if C * R < K:
    print(0)

else:
    num = 1
    c = 0
    r = 0
    d = 0
    while num <= K:
        if num == K:
            print(r + 1, c + 1, end=" ")
            break

        board[c][r] = num
        nx = c + direction[d][0]
        ny = r + direction[d][1]

        # 범위 밖이거나 이미 방문한 경우 -> 방향 전환
        if (nx < 0 or nx >= R or ny < 0 or ny >= C) or (board[nx][ny] != 0):
            d = (d + 1) % 4
            nx = c + direction[d][0]
            ny = r + direction[d][1]

        c = nx
        r = ny

        num += 1
