# 백준 26530번 Shipping
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    x = int(put())
    money = 0

    while x:
        x -= 1
        data = put().split()
        money += float(data[1]) * float(data[2])

    print("${:.2f}".format(money))