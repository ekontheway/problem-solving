import sys
input = sys.stdin.readline

N = int(input())
lst = [str(input().strip())[::-1] for _ in range(N)]
size = len(lst[0])
answer = 0

for cnt in range(1, size+1):
    sets = set()
    for num in lst:
        sets.add(num[:cnt])
    if (len(sets) == N):
        answer = cnt
        break
print(cnt)
