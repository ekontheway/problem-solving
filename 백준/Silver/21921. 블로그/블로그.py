n, x = map(int, input().strip().split(' '))
visits = list(map(int, input().strip().split()))

answer = sum(visits[0:x])
during = 1
total = answer
for i in range(1, n-x+1):
    total = total - visits[i-1] + visits[i+x-1]
    if (total > answer):
        answer = total
        during = 1
    elif (total == answer):
        during += 1

if (answer == 0):
    print('SAD')
else:
    print(answer, during, sep='\n')
