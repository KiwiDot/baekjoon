# 백준 15239번 Password check
import sys
put = sys.stdin.readline

N = int(put())
lowercase = set([chr(i + 97) for i in range(26)])
uppercase = set([chr(i + 65) for i in range(26)])
digit = set([str(i) for i in range(10)])
symbol = set("+_)(*&^%$#@!./,;{}")

while N:
    N -= 1
    S = int(put())
    s = set(put().strip())
    check = True

    if S < 12:
        check = False

    if not s & lowercase:   # 적어도 하나 이상의 소문자
        check = False

    if not s & uppercase:   # 적어도 하나 이상의 대문자
        check = False

    if not s & digit:       # 적어도 하나 이상의 숫자
        check = False

    if not s & symbol:      # 적어도 하나 이상의 기호
        check = False

    if check:
        print("valid")
    else:
        print("invalid")