import sys
input = sys.stdin.readline

S, E, Q = input().strip().split()

answer = 0

SH, SM = S.split(':')
EH, EM = E.split(':')
QH, QM = Q.split(':')

STotal = int(SH) * 60 + int(SM)
ETotal = int(EH) * 60 + int(EM)
QTotal = int(QH) * 60 + int(QM)

checks = {}

while True:
    line = input().strip()
    if not line:
        break

    time, student = line.split()
    timeH, timeM = time.split(':')
    timeTotal = int(timeH) * 60 + int(timeM)

    # 출석 시작
    if (0 <= timeTotal <= STotal):
        checks[student] = False

    # 출석 끝
    if (ETotal <= timeTotal <= QTotal
            and student in checks):
        checks[student] = True


for name, isCheck in checks.items():
    if (isCheck):
        answer += 1

print(answer)
