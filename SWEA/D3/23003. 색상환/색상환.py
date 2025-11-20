T = int(input())


for test_case in range(1, T+1):
    colors = {
        'red': [['purple', 'orange'], 'green'],
        'orange': [['red', 'yellow'], 'blue'],
        'yellow': [['green', 'orange'], 'purple'],
        'green': [['yellow', 'blue'], 'red'],
        'blue': [['purple', 'green'], 'orange'],
        'purple': [['red', 'blue'], 'yellow']
    }

    a, b = input().strip().split()
    answer = ''
    if (a == b):
        answer = 'E'
    elif (b in colors[a][0]):
        answer = 'A'
    elif (b in colors[a][1]):
        answer = 'C'
    else:
        answer = 'X'

    print(answer)
