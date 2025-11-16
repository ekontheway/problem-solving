T = int(input())

for test_case in range(1, T+1):
    n, m, k = map(int, input().strip().split())
    person = list(map(int, input().strip().split()))
    person.sort()

    answer = 'Possible'
    isPossible = True
    snack = 0
    idx = 0
    for time in range(person[-1]+1):
        # 붕어빵 생성
        if (time > 0 and time % m == 0):
            snack += k

        # 손님 도착
        if (person[idx] == time):
            # 붕어빵 존재O
            if (snack > 0):
                snack -= 1
                idx += 1
            # 붕어빵 존재X
            else:
                isPossible = False
                answer = 'Impossible'

        if (not isPossible):
            break

    print(f'#{test_case}', answer)
