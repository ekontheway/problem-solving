for test_case in range(1, 11):
    n = int(input())
    apt = list(map(int, input().strip().split()))

    answer = 0
    for dong in range(2, n-2):
        if (apt[dong] > apt[dong+2]
            and apt[dong] > apt[dong+1]
                and apt[dong] > apt[dong-1]
                and apt[dong] > apt[dong-2]):
            answer += apt[dong] - max(apt[dong-2], apt[dong-1], apt[dong+1], apt[dong+2])

    print(f'#{test_case}', answer)
