def solution(dirs):
    answer = set()
    
    dir = {
        'U' : [0, 1], "D" : [0, -1], "R" : [1, 0], "L" : [-1, 0]
    }
    
    road = [0,0]
    for d in dirs:
        currX = road[0]
        currY = road[1]
        
        road[0] += dir[d][0] 
        road[1] += dir[d][1]
        
        if(road[0] > 5 or road[0] < -5 or road[1] > 5 or road[1] < -5):
            road[0] = currX
            road[1] = currY
            continue
        
        answer.add((road[0], road[1], currX, currY))
        answer.add((currX, currY, road[0], road[1]))
           
    return len(answer)//2