import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

dic = {}
for _ in range(N):
    ch = input().rstrip()
    if (len(ch) < M):
        continue
    if (ch in dic):
        dic[ch] += 1
    else:
        dic[ch] = 1
sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, cnt in sorted_dic:
    print(word)
