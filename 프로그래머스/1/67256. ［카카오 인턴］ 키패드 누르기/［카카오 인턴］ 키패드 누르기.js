function solution(numbers, hand) {
    var answer = '';
    
    let lefts = {
          1: [0, 0], 4: [1, 0], 7: [2, 0]
    };
    let rights = {
          3: [0, 2], 6: [1, 2], 9: [2, 2],
    };
    let centers = {
          2: [0, 1], 5: [1, 1], 8: [2, 1], 0: [3, 1],
    };
    
    let leftIdx = [3,0]
    let rightIdx = [3,2]
    
    for (let num of numbers){
        // 왼쪽 키패드
        if(num in lefts){
            answer += 'L'
            leftIdx = lefts[num]
        }
        // 오른쪽 키패드
        else if (num in rights){
            answer += 'R'
            rightIdx = rights[num]
        }
        // 가운데 키패드
        else{
            let targetIdx = centers[num]
            let diffLeft = Math.abs(centers[num][0] - leftIdx[0]) + Math.abs(centers[num][1] - leftIdx[1]) 
            let diffRight = Math.abs(centers[num][0] - rightIdx[0]) + Math.abs(centers[num][1] - rightIdx[1])
            
            if(diffLeft == diffRight){
                if(hand == 'right'){
                    answer += 'R'
                    rightIdx = targetIdx
                }
                else{
                    answer += 'L'
                    leftIdx = targetIdx
                }
            }
            else if(diffLeft < diffRight){
                answer += 'L'
                leftIdx = targetIdx
            }
            else{
                answer += 'R'
                rightIdx = targetIdx
            }
        }
    }
    return answer;
}