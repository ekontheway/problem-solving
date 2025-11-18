for test_case in range(1, 11):
    n = int(input())
    patterns = list(input().strip())
    answer = 1

    stack = []
    dic = {'{': '}', '}': '{', '(': ')', ')': '(',
           '[': ']', ']': '[', '<': '>', '>': '<'}
    openPatterns = '[(<{'

    for i in range(n):
        if (patterns[i] in openPatterns):
            stack.append(patterns[i])
        else:
            if (len(stack) == 0):
                answer = 0
            if (stack[-1] == dic[patterns[i]]):
                stack.pop()
            else:
                answer = 0

        if (answer == 0):
            break

    if (len(stack) != 0):
        answer = 0

    print(f'#{test_case}', answer)
