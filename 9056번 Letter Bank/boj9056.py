# 백준 9056번 Letter Bank
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    a, b = put().split()

    if set(a) == set(b):
        print("YES")
    else:
        print("NO")