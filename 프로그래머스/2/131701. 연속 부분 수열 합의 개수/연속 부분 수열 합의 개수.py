def solution(elements):
    # 원소 1개씩의 합
    answer = set(elements)
    # 원소 총합
    answer.add(sum(elements))
    
    # 원소 2개 이상~수열 길이-1 의 합
    new_elements = elements + elements
    for cnt in range(2, len(elements)):
        for i in range(0, len(elements)):
            total = sum(new_elements[i:i+cnt])
            answer.add(total)  
                
    return len(answer)