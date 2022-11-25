# 백준 13064번 Cameras
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    number = put().strip()
    n4 = number[4]
    num = number[:4] + number[5:]
    check = True

    if num[0] != num[1]:
        check = False

    if not num.isdigit():
        check = False

    if '0' in num:
        check = False

    if not n4.isalpha() or n4.islower():
        check = False

    if check:
        print(number)
