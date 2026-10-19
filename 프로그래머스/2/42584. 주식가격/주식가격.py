def solution(prices):
    answer = [0] * len(prices)
    
    stack = []
    curr = 0
    while(curr<len(prices)):
        if(not stack):
            stack.append(curr)
            curr += 1
            continue
        top = stack[-1]
        if(prices[top] > prices[curr]):
            answer[top] = curr - stack.pop()
        else:
            stack.append(curr)
            curr += 1
            
    # 스택 남은 인덱스 처리
    for idx in range(len(stack)):
        answer[stack[idx]] = len(prices) - stack[idx] -1
   
    return answer