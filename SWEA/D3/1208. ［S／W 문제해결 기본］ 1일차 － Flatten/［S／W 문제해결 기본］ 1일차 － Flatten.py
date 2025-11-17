for test_case in range(1, 11):
    n = int(input())
    nums = list(map(int, input().strip().split()))
    nums.sort()

    i = 0
    while (i < n and max(nums)-min(nums) > 1):
        nums.sort()
        nums[-1] -= 1
        nums[0] += 1
        i += 1

    print(f'#{test_case}', max(nums)-min(nums))
