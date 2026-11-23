import sys
input = sys.stdin.readline

xs = {}
ys = {}

for _ in range(3):
    x, y = map(int, input().strip().split())

    if (x in xs):
        xs[x] += 1
    else:
        xs[x] = 1

    if (y in ys):
        ys[y] += 1
    else:
        ys[y] = 1

answer = []
for nx in xs:
    if (xs[nx] == 1):
        answer.append(nx)
for ny in ys:
    if (ys[ny] == 1):
        answer.append(ny)

print(*answer)
