function solution(progresses, speeds) {
    let days = []
    for (let i = 0; i<progresses.length; i++){
        days.push(Math.ceil((100-progresses[i])/speeds[i]))
    }
    
    let maxDays = days[0]
    let release = {
        [maxDays] : 1
    };
    
    for (let d = 1; d<progresses.length; d++){
        if(days[d]<=maxDays){
            release[maxDays] += 1
        }
        else{
            release[days[d]] = 1
            maxDays = days[d]
        }
    }
       
    return Object.values(release);
}