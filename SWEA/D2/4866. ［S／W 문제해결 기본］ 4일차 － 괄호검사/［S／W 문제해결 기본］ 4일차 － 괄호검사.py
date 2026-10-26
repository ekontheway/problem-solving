
T = int(input())

for test_case in range(1, T + 1):
    inputs = input().strip()
  
    stack = []
    pattern = '(){}[]'

    opens = {'[' : ']' ,'(' : ')','{' : '}'}
    close = {']' : '[',  ')' : '(',  '}' : '{' }
    
    isCorrect = 1
    for c in inputs:
        # 연 괄호 경우
        if(c in opens):
            stack.append(c)
        # 닫는 괄호 검사
        if(c in close):
            # 빈 스택일경우 or 짝이 맞지 않을 경우
            if(not stack or opens[stack[-1]] != c):
                isCorrect = 0
                break
            # 짝이 맞을 경우
            else:
                stack.pop()

            
    if(len(stack) > 0):
        isCorrect = 0
        
    if(isCorrect):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')