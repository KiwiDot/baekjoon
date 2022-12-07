# 백준 1730번 판화
import sys
put = sys.stdin.readline


def moving(x, y, d1, d2):
    if answer[x][y] == '+':
        pass
    elif answer[x][y] == d2:
        answer[x][y] = '+'
    else:
        answer[x][y] = d1


N = int(put())
move = put().strip()
answer = [['.' for i in range(N)] for j in range(N)]
x = y = 0

for i in move:
    if i == 'U' and x > 0:
        moving(x, y, '|', '-')
        x -= 1
        moving(x, y, '|', '-')

    elif i == 'D' and x < N - 1:
        moving(x, y, '|', '-')
        x += 1
        moving(x, y, '|', '-')

    elif i == 'L' and y > 0:
        moving(x, y, '-', '|')
        y -= 1
        moving(x, y, '-', '|')

    elif i == 'R' and y < N - 1:
        moving(x, y, '-', '|')
        y += 1
        moving(x, y, '-', '|')

for i in answer:
    print(''.join(i))