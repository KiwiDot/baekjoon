# 백준 26645번 성장의 비약 선택권
import sys
put = sys.stdin.readline

N = int(put())

if N < 206:
    print(1)

elif N < 218:
    print(2)

elif N < 229:
    print(3)

else:
    print(4)