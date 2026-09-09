def solution(clothes):
    # 옷장 만들기
    closet = {}
    for item, cate in clothes:
        if(cate not in closet):
            closet[cate] = [item]
        else:
            closet[cate].append(item)
    
    # 안입는 경우까지 포함해 모든 경우의 수 곱
    answer = 1
    for cate in closet:
        answer *= (len(closet[cate])+1)      
    
    # 모든 옷을 안 입는 경우 제외
    return answer - 1