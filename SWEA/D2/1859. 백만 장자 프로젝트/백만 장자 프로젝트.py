T = int(input())


for test_case in range(1, T+1):

    N = int(input())
    lst = list(map(int, input().split()))

    answer = 0

    target = N -1
    curr = N-2
    for i in range(curr, -1, -1):
        if(lst[i] > lst[target]):
            target = i
            continue
        else:
            answer += (lst[target] - lst[i])

    print(f'#{test_case}', answer)
