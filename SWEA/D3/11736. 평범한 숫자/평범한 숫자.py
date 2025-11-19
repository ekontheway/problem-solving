T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    pi = list(map(int, input().strip().split()))
    answer = 0
    for i in range(1, n-1):
        if (pi[i-1] < pi[i] < pi[i+1] or pi[i-1] > pi[i] > pi[i+1]):
            answer += 1

    print(f'#{test_case}', answer)
