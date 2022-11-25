# 백준 13064번 Cameras
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    num = put().strip()
    check = True

    # 맨 앞 두 자리는 동일한 숫자여야 한다.
    if num[0] != num[1] or not num[0].isdigit() or '0' == num[0]:
        check = False

    # 세 네 번째 자리가 두 자리 숫자여야 한다.
    if not num[2:4].isdigit() or '0' in num[2:4]:
        check = False

    # 다섯 번째 자리가 대문자여야 한다.
    if not num[4].isalpha() or num[4].islower():
        check = False

    # 뒤 세 자리가 숫자여야 한다.
    if not num[5:].isdigit() or '0' in num[5:]:
        check = False

    if check:
        print(num)