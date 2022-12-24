# 백준 26767번 Hurra!
import sys
put = sys.stdin.readline

N = int(put())

for i in range(1, N+1):
    if not i % 77:
        print("Wiwat!")

    elif not i % 7:
        print("Hurra!")

    elif not i % 11:
        print("Super!")

    else:
        print(i)