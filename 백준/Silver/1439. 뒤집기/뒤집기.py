import sys
input = sys.stdin.readline

S = list(input().strip())

nums = {"0": 0, "1": 0}
before = S[0]
nums[before] += 1
for n in range(1, len(S)):
    if (S[n] != before):
        before = S[n]
        nums[before] += 1

print(min(nums['0'], nums['1']))
