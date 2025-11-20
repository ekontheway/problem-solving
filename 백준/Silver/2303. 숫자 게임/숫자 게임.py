from itertools import combinations

n = int(input())
answer = []
for idx in range(n):
    lst = list(map(int, input().strip().split()))

    big = 0
    for j in combinations(lst, 3):
        total = str(j[0]+j[1]+j[2])[-1]
        if (int(total) > big):
            big = int(total)

    answer.append([idx+1, big])

answer = sorted(answer, key=lambda x: (x[1], x[0]), reverse=True)
print(answer[0][0])