T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    
    sums = [0]
    for num in arr:
        new_sums = []
        for s in sums:
            new_sums.append(s + num)
        sums += new_sums
        
    answer = 0
    for item in sums:
        if(item == K):
            answer += 1    
            
    print(f'#{test_case} {answer}')