T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    print(f'#{test_case} {arr[M%N]}')