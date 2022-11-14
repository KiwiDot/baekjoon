# 백준 8713번 Znak działania
import sys
put = sys.stdin.readline

a, b = map(int, put().split())
a = str(a) if a > 0 else "({})".format(a)
b = str(b) if b > 0 else "({})".format(b)

answer = {}

for i in ['+', '-', '*']:
    answer[a + i + b] = eval(a + i + b)

if list(answer.values()).count(max(answer.values())) == 1:
    i = max(answer, key=answer.get)
    result = str(answer[i]) if answer[i] > 0 else "({})".format(answer[i])
    print(i + '=' + result)
else:
    print("NIE")