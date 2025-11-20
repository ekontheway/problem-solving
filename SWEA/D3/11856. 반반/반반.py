T = int(input())

for test_case in range(1, T+1):
    dic = dict()
    s = list(input().strip())
    for ch in s:
        if (ch in dic):
            dic[ch] += 1
        else:
            dic[ch] = 1

    answer = 'Yes'
    for ch, cnt in dic.items():
        if (cnt != 2):
            answer = 'No'
            break

    print(f'#{test_case}', answer)
