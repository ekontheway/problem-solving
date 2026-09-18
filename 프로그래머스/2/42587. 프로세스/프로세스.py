def solution(priorities, location):
    answer = [0] * len(priorities)
    
    Q = []
    for i in range(len(priorities)):
        Q.append([i, priorities[i]])
    
    st = 0
    en = len(priorities)
    cnt = 1
    # 큐가 비기 전까지 반복 (st랑 en 값이 같아지기 전까지)
    while(st!=en):
        max_num = max([m[1] for m in Q[st:en]])
        
        # 우선순위 낮을 경우, 다시 큐에 넣음
        if(Q[st][1]<max_num):
            en += 1
            Q.append([Q[st][0], Q[st][1]])
        else:
            answer[Q[st][0]] = cnt
            cnt += 1

        st += 1
            
    return answer[location]