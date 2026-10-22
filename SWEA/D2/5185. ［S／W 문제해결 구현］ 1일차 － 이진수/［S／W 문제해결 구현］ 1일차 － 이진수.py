T = int(input())

for test_case in range(1, T + 1):
    N, arr = input().strip().split()
    
    answer = ''
    for i in range(int(N)):
        # 16 진수 -> 10 진수  -> 2 진수
        total = bin(int(arr[i], 16))[2:]        
        # 자리 맞춤
        total = '0' * (4-len(total)) + total
        answer += total         
    
    print(f'#{test_case} {answer}')