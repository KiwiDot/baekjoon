# 백준 5357번 Dedupe
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    text = put().strip()
    answer = "-"

    for i in text:
        if answer[-1] != i:
            answer += i

    print(answer[1:])