# 백준 26863번 Absolutely Flat
import sys
put = sys.stdin.readline

a = sorted([int(put()) for i in range(4)])
b = int(put())
check = False

if len(set(a)) == 1:
    check = True

else:
    a[0] += b
    if len(set(a)) == 1:
        check = True

print(int(check))