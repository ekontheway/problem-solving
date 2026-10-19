def solution(genres, plays):
    answer = []
    
    album = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        if(g in album):
            album[g][0] += p
            album[g][1].append([p,i])
        else:
            album[g] = [p, [[p, i]]]
    
    # 장르별 내림차순 -> 재생횟수 내림차순 -> 고유번호 오름차순
    sort_album = sorted(album.items(), key=lambda x : -x[1][0])
    for g in sort_album:
        g[1][1].sort(key=lambda x : (-x[0], x[1]))
        
        for song in g[1][1][:2]:
            answer.append(song[1])
            
    return answer