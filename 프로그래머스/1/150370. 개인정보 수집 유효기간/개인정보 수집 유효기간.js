function solution(today, terms, privacies) {
    let answer = [];
    
    // 약관 파싱
    let validOptions = {}
    for (let v of terms){
        let [option, month] = v.split(' ')
        validOptions[option] = Number(month)
    }

    let idx = 1
    for (let p of privacies){
        let [numbers, option] = p.split(' ')
        // 날짜 계산
        let [year, month, date] = numbers.split('.');
        let [t_year, t_month, t_date] = today.split('.');
        
        let convert_today = Number(t_year)*12*28 + Number(t_month)*28 + Number(t_date);
        let target = Number(year)*12*28 + Number(month) * 28 + Number(date) + validOptions[option]*28 - 1
        
        // 오늘과 비교
        if(convert_today > target){
            answer.push(idx)
        }
        idx += 1        
    }
    return answer;
}