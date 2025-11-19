T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().strip().split())
    a = set(input().strip().split(' '))
    b = set(input().strip().split(' '))

    print(f'#{test_case}', len(a.intersection(b)))
