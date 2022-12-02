# 백준 11576번 Base Conversion
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
m = int(put())
num = [int(_) for _ in put().split()]
a = 0

# 미래세계의 A진법 숫자를 현대의 10진수로 변환
for i in range(m):
    a += num[i] * A ** (m - i - 1)

# 10진수를 정이가 사용하는 B진법 숫자로 변환
num = []
while a > 0:
    a, n = divmod(a, B)
    num.append(str(n))

print(' '.join(num[::-1]))