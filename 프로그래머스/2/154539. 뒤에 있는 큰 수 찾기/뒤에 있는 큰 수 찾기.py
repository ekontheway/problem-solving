def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [0]
    idx = 1
    while(stack and idx < len(numbers)):
        curr = numbers[idx]
        
        while(stack 
              and numbers[stack[-1]]<numbers[idx]):
            top = stack.pop()
            answer[top] = curr
        
        stack.append(idx)
        idx += 1
            
    return answer