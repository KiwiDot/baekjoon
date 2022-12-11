# 백준 26148번 세로 달력
import sys
put = sys.stdin.readline

N = int(put())
w = int(put())

if (not N % 4 and N % 100) or not N % 400:
    print(30)
else:
    print(29)