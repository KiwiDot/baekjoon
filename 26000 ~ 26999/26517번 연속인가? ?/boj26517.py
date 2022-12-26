# 백준 26517번 연속인가? ?
import sys
put = sys.stdin.readline

k = int(put())
a, b, c, d = map(int, put().split())

# 함수가 특정 구간에 연속이라면, 좌극한과 우극한이 같다
if a * k + b == c * k + d:
    print("Yes", a * k + b)
else:
    print("No")