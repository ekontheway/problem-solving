def isPalindrome(arr, n):
    total = 0
    for row in range(8):
        for col in range(8-n+1):
            if (arr[row][col:col+n] == arr[row][col:col+n][::-1]):
                total += 1
    return total

for test_case in range(1, 11):
    n = int(input())
    board = [list(input().strip()) for _ in range(8)]

    answer = 0
    # 가로 회문 검사
    answer += (isPalindrome(board, n))

    # 세로 회문 검사
    new_board = []
    for col in range(8):
        lst = []
        for row in range(8):
            lst.append(board[row][col])
        new_board.append(lst)
    answer += isPalindrome(new_board, n)

    print(f'#{test_case}', answer)
