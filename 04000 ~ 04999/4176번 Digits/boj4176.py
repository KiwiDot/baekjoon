# 백준 4176번 Digits
import sys
put = sys.stdin.readline

while True:
    x0 = put().strip()
    if x0 == "END":
        break
    i = 1

    while x0 != "1":
        x0 = str(len(x0))
        i += 1

    print(i)