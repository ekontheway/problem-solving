T = int(input())

for test_case in range(1, T + 1):
    num = float(input())
    
    answer = ''
    isOverflow = False
    while(num != 0):
        
        num *= 2
        answer += str(int(num))
        num -= int(num)
        
        if(len(answer)>12):
            isOverflow = True
            break
            
    if(isOverflow):
        print(f'#{test_case} overflow')
    else:
        print(f'#{test_case} {answer}')