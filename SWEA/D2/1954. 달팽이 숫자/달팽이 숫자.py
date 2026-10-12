T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    answer = [[0] * N for _ in range(N)]

    number = 1
    x = 0
    y = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0

    while (number <= N * N):
        # 현재 위치에 숫자 넣기
        answer[x][y] = number
        number += 1

        if (number > N*N):
            break

        # 다음 위치 확인
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 이동할 수 없을 경우 -> 방향 전환
        if (not (0 <= nx < N and 0 <= ny < N)
                or answer[nx][ny] != 0):
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

        x = nx
        y = ny

    print(f'#{test_case}')

    for row in answer:
        print(*row)
