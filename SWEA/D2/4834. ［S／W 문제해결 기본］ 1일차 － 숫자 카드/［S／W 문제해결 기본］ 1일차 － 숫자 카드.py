T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = input()
    nums = [0] * 10
    for i in range(N):
        nums[int(arr[i])] += 1
    cnt = max(nums)
    idx = nums[::-1].index(cnt)
    print(f'#{test_case} {9-idx} {cnt}')
       