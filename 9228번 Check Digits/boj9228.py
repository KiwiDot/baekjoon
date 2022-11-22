# 백준 9228번 Check Digits
import sys
put = sys.stdin.readline

while True:
    n = put().strip()[::-1]
    if n == '#':
        break

    check = 0
    for i in range(len(n)):
        check += int(n[i]) * (i+2)

    answer = 11 - check % 11
    if answer == 10:
        answer = "Rejected"
    elif answer == 11:
        answer = 0
    print("{} -> {}".format(n[::-1], answer))