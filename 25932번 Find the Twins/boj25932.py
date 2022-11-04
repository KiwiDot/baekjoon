# 백준 25932번 Find the Twins
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    num = put().split()
    print(' '.join(num))
    if "17" in num and "18" in num:
        print("both")

    elif "17" in num:
        print("zack")

    elif "18" in num:
        print("mack")

    else:
        print("none")

    print()