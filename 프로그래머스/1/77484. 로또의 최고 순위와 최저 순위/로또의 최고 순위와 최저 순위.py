def solution(lottos, win_nums):
    wins = 0
    zeros = lottos.count(0)
    for i in lottos:
        if(i in win_nums):
            wins +=1

    rank = {
        6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6
    }
    
    return [rank[wins+zeros], rank[wins]]