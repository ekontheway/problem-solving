for test_case in range(1, 11):
    n, nums = input().strip().split(' ')

    i = 0
    while (i < len(nums)-1):
        if (nums[i] == nums[i+1]):
            nums = nums[:i]+nums[i+2:]
            if (i != 0):
                i -= 1
        else:
            i += 1

    print(f'#{test_case}', nums)
