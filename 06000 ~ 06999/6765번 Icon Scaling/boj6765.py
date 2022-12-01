# 백준 6765번 Icon Scaling
import sys
put = sys.stdin.readline

k = int(put())
icon = ["*x*", " xx", "* *"]

for i in range(3):
    icon[i] = ''.join([_ * k for _ in icon[i]])

for i in icon:
    for j in range(k):
        print(i)