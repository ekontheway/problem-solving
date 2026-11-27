from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().strip().split()))
lst = reversed(lst)
answer = deque()
num = 1
for idx in lst:
    # 1 : 제일 윗 카드
    if (idx == 1):
        answer.appendleft(num)
    # 2 : 위에서 2번째 카드
    elif (idx == 2):
        first = answer.popleft()
        answer.appendleft(num)
        answer.appendleft(first)
    # 3 : 마지막 카드
    elif (idx == 3):
        answer.append(num)
    num += 1

print(*answer)
