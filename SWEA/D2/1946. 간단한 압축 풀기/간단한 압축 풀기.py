T = int(input())

for test_case in range(1, T + 1):        
    n = int(input())
    strings = ''
    for _ in range(n):
        c, k = input().strip().split()
        strings += c * int(k)
        
    print(f'#{test_case}')
    for i in range(0, len(strings), 10):
        print(strings[i:i+10])