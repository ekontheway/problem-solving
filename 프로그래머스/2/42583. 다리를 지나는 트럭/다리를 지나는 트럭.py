def solution(bridge_length, weight, truck_weights):
    answer = 0
    end = []
    ing = []
    truckIdx = 0
    ingIdx = 0
    timeIdx = 1
    
    # 다리를 완전히 지날때까지 반복
    while(len(end) < len(truck_weights)):        
        #1. 다리를 다 건넌 트럭이 있는지 확인하고 end로 이동
        if(ing and timeIdx-ing[ingIdx][1] >= bridge_length):
            end.append(ing[ingIdx])
            ingIdx += 1
            if(len(end) == len(truck_weights)):
                answer = timeIdx
        
        sums = sum(t[0] for t in ing[ingIdx:])
        #2. 다음 트럭이 남아 있는지 확인
        if (truckIdx < len(truck_weights)
            and len(ing) - ingIdx < bridge_length
            and sums + truck_weights[truckIdx] <= weight):
            ing.append([truck_weights[truckIdx], timeIdx])
            truckIdx += 1

        timeIdx += 1
        
    return answer