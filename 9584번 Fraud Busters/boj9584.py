# 백준 9584번 Fraud Busters
import sys
put = sys.stdin.readline

code = put().strip()
n = int(put())
k = 0
answer = []

while n:
    n -= 1
    c = put().strip()
    check = True

    for i in range(9):
        if code[i] == '*':
            continue

        if code[i] != c[i]:
            check = False
            break

    if check:
        k += 1
        answer.append(c)

print(k)
for i in answer:
    print(i)