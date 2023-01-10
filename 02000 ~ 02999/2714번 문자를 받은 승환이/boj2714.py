# 백준 2714번 문자를 받은 승환이
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    R, C, msg = put().split()
    R, C = int(R), int(C)
    msg = [msg[i*C:i*C+C] for i in range(R)]
    RC = R * C
    answer = ""

    # 좌표 저장
    x, y = [-1], [0]
    r, c = [R-1], [C]

    # 방향
    d = 'R'
    move = {'R': [x, c, 1, 'D'],    # x 좌표가 c만큼 양의 방향으로, 다음 방향은 D
            'D': [y, r, 1, 'L'],    # y 좌표가 r만큼 양의 방향으로, 다음 방향은 L
            'L': [x, c, -1, 'U'],   # x 좌표가 c만큼 음의 방향으로, 다음 방향은 U
            'U': [y, r, -1, 'R']}   # y 좌표가 r만큼 음의 방향으로, 다음 방향은 R

    while RC:
        # 달팽이 배열
        xy, rc, d1, nxt = move[d]

        for i in range(rc[0]):
            RC -= 1
            xy[0] += d1
            answer += msg[y[0]][x[0]]

        d = nxt
        rc[0] -= 1

    # 문자열 해독
    answer = [answer[i*5:i*5+5] for i in range(len(answer)//5)]
    for i in range(len(answer)):
        a = int(answer[i], 2)
        if a:
            answer[i] = chr(a+64)
        else:
            answer[i] = ' '

    print(''.join(answer).rstrip())