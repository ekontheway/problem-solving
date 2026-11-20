N = int(input())

for _ in range(N):
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    answer = "D"
    aLst = [0] * 4
    bLst = [0] * 4

    # 각각 모양 개수 카운트
    for i in a[1:]:
        aLst[4 - i] += 1
    for j in b[1:]:
        bLst[4 - j] += 1

    # a 과 b 비교
    for t in range(4):
        if aLst[t] > bLst[t]:
            answer = "A"
            break
        elif aLst[t] < bLst[t]:
            answer = "B"
            break

    print(answer)
