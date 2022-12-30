# 백준 4246번 To and Fro
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break
    text = put().strip()
    answer = ["" for i in range(n)]

    for i in range(len(text)//n):
        if i % 2:
            for j in range(n):
                answer[n-j-1] += text[i*n+j]
        else:
            for j in range(n):
                answer[j] += text[i*n+j]

    print(''.join(answer))