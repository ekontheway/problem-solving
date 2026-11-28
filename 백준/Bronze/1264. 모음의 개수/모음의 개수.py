targets = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    answer = 0
    s = input().strip()

    if (s == '#'):
        break

    for i in s:
        if (i in targets):
            answer += 1

    print(answer)
