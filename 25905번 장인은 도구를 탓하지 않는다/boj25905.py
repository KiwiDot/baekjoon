# 백준 25905번 장인은 도구를 탓하지 않는다
import sys
put = sys.stdin.readline

p = sorted([float(put()) for i in range(10)], reverse=True)[:9]
x = 362880
answer = 1

for i in p:
    answer *= i * 10

print(answer / x)