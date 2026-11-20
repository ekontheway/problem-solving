N = int(input())
lst = list(map(int, input().strip().split()))
inc, dec, ans = 1, 1, 1
for i in range(1, N):
    if lst[i - 1] <= lst[i]:
        inc += 1
    else:
        inc = 1

    if lst[i - 1] >= lst[i]:
        dec += 1
    else:
        dec = 1

    ans = max(ans, dec, inc)

print(ans)