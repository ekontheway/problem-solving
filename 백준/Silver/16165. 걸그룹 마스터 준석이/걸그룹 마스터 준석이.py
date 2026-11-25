import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

girls = {}
for _ in range(N):
    gr = input().strip()
    girls[gr] = []
    cnt = int(input())
    for _ in range(cnt):
        name = input().strip()
        girls[gr].append(name)

for _ in range(M):
    q = input().strip()
    num = int(input())

    # 0 -> input : 팀 -> output : 멤버 이름 사전순 한 줄 한 명씩
    # 1 -> input : 멤버 -> output : 해당 멤버 속한 팀명
    if (num == 0):
        team = sorted(girls[q])
        print(*team, sep='\n')
    else:
        for g, m in girls.items():
            if (q in m):
                print(g)
