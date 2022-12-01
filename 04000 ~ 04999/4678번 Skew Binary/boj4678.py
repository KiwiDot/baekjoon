# 백준 4678번 Skew Binary
import sys
put = sys.stdin.readline

while True:
    n = put().strip()
    if n == '0':
        break
    answer = 0

    for i in range(len(n)):
        answer += int(n[i]) * (2 ** (len(n) - i) - 1)

    print(answer)