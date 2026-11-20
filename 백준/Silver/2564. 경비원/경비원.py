R, C = map(int, input().strip().split())
N = int(input())
stores = [list(map(int, input().strip().split())) for _ in range(N)]
targetX, targetY = map(int, input().strip().split())
answer = 0
total = 2 * (R + C)
if targetX == 1:
    dg = targetY
elif targetX == 4:
    dg = R + targetY
elif targetX == 2:
    dg = R + C + R - targetY
else:
    dg = 2 * (R + C) - targetY

for items in stores:
    nx, ny = items
    st = 0
    if nx == 1:
        st = ny
    elif nx == 4:
        st = R + ny
    elif nx == 2:
        st = R + C + R - ny
    else:
        st = 2 * (R + C) - ny

    diff = abs(st - dg)
    answer += min(diff, total - diff)
print(answer)
