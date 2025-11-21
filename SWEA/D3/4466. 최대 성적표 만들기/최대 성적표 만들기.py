T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().strip().split())
    scores = list(map(int, input().strip().split()))

    scores.sort(reverse=True)
    answer = sum(scores[:k])
    print(f'#{test_case}', answer)
