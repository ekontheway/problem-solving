def solution(topping):
    answer = 0
    
    rights = [0] * 10001
    for t in topping:
        rights[t] += 1
    
    lefts = set()
    right_cnt = len(set(topping))
    for t in topping:
        if(len(lefts)==right_cnt):
            answer += 1
            
        lefts.add(t)
        rights[t] -= 1        
        if(rights[t]==0):
            right_cnt -= 1
        

    return answer