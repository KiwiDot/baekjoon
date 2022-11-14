# 백준 16634번 Run-Length Encoding, Run!
import sys
put = sys.stdin.readline

letter, msg = put().split()

if letter == 'E':
    answer = ""
    cnt = 0
    for i in msg:
        if not answer:
            answer += i
            cnt = 1

        elif answer[-1] == i:
            cnt += 1

        else:
            answer += str(cnt) + i
            cnt = 1

    answer += str(cnt)

else:
    answer = ""
    for i in range(0, len(msg), 2):
        answer += msg[i] * int(msg[i+1])

print(answer)