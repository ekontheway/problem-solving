import sys
input = sys.stdin.readline

a, b, c = map(int, input().strip().split())
lst = sorted([a, b, c], reverse=True)

while (lst[0] >= lst[1]+lst[2]):
    lst[0] -= 1
print(sum(lst))
