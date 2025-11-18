n, k = map(int, input().strip().split(' '))
lst = list(map(int, input().strip().split()))

left, right = 0, k
total = sum(lst[:k])
answer = total

while (right < n):
    total += lst[right]
    total -= lst[left]
    left += 1
    right += 1
    answer = max(answer, total)

print(answer)