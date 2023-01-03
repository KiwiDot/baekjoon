# 백준 15235번 Olympiad Pizza
import sys
put = sys.stdin.readline

N = int(put())
pizza = [int(_) for _ in put().split()]
answer = [''] * N
cnt = 0

while set(pizza) != {0}:
    for i in range(N):
        if pizza[i]:
            cnt += 1
            pizza[i] -= 1

            if not pizza[i]:
                answer[i] = str(cnt)

print(' '.join(answer))