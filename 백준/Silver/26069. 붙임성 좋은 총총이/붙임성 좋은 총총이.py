import sys
input = sys.stdin.readline

N = int(input())

dances = {'ChongChong': True}
for _ in range(N):
    A, B = input().strip().split(' ')

    # A, B 둘 중 총총일 경우
    if (A is 'ChongChong'):
        dances[B] = True
    elif (B is 'ChongChong'):
        dances[A] = True
    # A, B 총총이 아닐 경우
    else:
        if (A in dances):
            dances[B] = True
        elif (B in dances):
            dances[A] = True

answer = 0
for name, d in dances.items():
    if (d):
        answer += 1
print(answer)
