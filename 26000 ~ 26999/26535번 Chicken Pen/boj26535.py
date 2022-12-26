# 백준 26535번 Chicken Pen
import sys
put = sys.stdin.readline

n = int(put())
pen = 0

while True:
    pen += 1
    if n <= pen ** 2:
        break

print('x' * (pen+2))
for i in range(pen):
    print('x' + '.' * pen + 'x')
print('x' * (pen+2))