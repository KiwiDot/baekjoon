# 백준 20282번 Game Show!
import sys
put = sys.stdin.readline

C = int(put())
money = [100]

while C:
    C -= 1
    V = int(put())
    money.append(money[-1] + V)

print(max(money))