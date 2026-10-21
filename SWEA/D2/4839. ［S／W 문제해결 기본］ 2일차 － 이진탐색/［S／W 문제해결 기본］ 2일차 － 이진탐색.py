def binarySearch(page, target):
    cnt = 0
    l = 1
    r = p
    mid= int((l+r)/2)
    while(mid!=target):
        cnt += 1
        if(mid<target):
            l = mid
        elif(mid>target):
            r = mid
        else:
            break
        mid= int((l+r)/2)
    return cnt
    

T = int(input())
for test_case in range(1, T + 1):
    p, a, b = map(int, input().strip().split())
    cntA = binarySearch(p, a)
    cntB = binarySearch(p, b)
    if(cntA >cntB):
        print(f'#{test_case} B')
    elif(cntA < cntB):
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')