T = int(input())

for test_case in range(1, T + 1):
    arr = input().strip().split()
    
    stack = []
    operator = '+-*/'
    for c in arr:
        # 연산자 일경우
        if(c in operator):
            if(len(stack) == 1):
                print(f'#{test_case} error')
                break
            n1 = stack.pop()
            n2 = stack.pop()
            if (c=='+'):
                stack.append(n1+ n2)                
            elif(c=='-'):
                stack.append(n2 - n1)
            elif(c=='/'):
                stack.append(int(n2 / n1))
            else:
                stack.append(n1 * n2)
        # 끝맺음 . 나올경우
        elif(c=='.'):
            if(len(stack)==1):
                print(f'#{test_case} {stack[0]}')
            else:
                print(f'#{test_case} error')
            break
        # 숫자가 나올경우
        else:
            stack.append(int(c))
           