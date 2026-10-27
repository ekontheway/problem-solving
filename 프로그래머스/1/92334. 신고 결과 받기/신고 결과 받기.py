def solution(id_list, report, k):
    answer = []
    sue = {}
    result = {}
    tup = set()
    for inputs in report:
        a, b = inputs.split() 
        if((a,b) in tup):
            continue
        if(a in sue):
            sue[a].append(b)
        else:
            sue[a] = [b]
        if(b in result):
            result[b] += 1
        else:
            result[b] = 1
        tup.add((a,b))
    
    alarms = []
    for key, items in result.items():
        if(items>=k):
            alarms.append(key) 
        
    for id in id_list:
        nums = 0
        if(id not in sue):
            answer.append(0)
            continue
        for r in alarms:
            if(r in sue[id]):
                nums += 1
        answer.append(nums)

    return answer