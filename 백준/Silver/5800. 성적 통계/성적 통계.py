import sys
input = sys.stdin.readline

K = int(input())
for test in range(1, K+1):
    lst = list(map(int, input().strip().split()))
    K = lst[0]
    scores = lst[1:]
    scores.sort(reverse=True)

    gp = float('-inf')
    for idx in range(K-1):
        gp = max(gp, abs(scores[idx]-scores[idx+1]))

    print(f'Class {test}')
    print(f'Max {max(scores)}, Min {min(scores)}, Largest gap {gp}')
