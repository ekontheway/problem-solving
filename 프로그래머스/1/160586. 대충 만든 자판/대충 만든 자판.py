def solution(keymap, targets):
    answer = []
    
    keyboard = {}
    for keys in keymap:
        for ch in keys:
            if (ch in keyboard):
                keyboard[ch] = min(keys.index(ch)+1, keyboard[ch])
            else:
                keyboard[ch] = keys.index(ch)+1
    
    for target in targets:
        cnt = 0
        for alpha in target:
            if(alpha not in keyboard):
                cnt = -1
                break
            cnt += keyboard[alpha]
        answer.append(cnt)            
    
    return answer