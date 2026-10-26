T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().strip().split())
    tree = [[] for _ in range(E+2)]
    
    inputs = list(map(int, input().strip().split()))
    for i in range(0,E*2,2):
        p, c = inputs[i], inputs[i+1]
        tree[p].append(c)
    
    stack = [N]
    answer = 0
    
    while(stack):
        curr = stack.pop()
        answer += 1
        
        for ch in tree[curr]:
            stack.append(ch)    
    
    print(f'#{test_case} {answer}')