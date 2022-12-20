# 백준 5292번 Counting Swann’s Coins
import sys
put = sys.stdin.readline

coin = int(put())

for i in range(1, coin+1):
    if not i % 15:
        print("DeadMan")
    elif not i % 3:
        print("Dead")
    elif not i % 5:
        print("Man")
    else:
        print(i, end=' ')