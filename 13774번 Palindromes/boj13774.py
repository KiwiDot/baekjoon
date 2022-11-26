# 백준 13774번 Palindromes
import sys
put = sys.stdin.readline

while True:
    text = put().strip()
    if text == '#':
        break
    check = True

    for i in range(len(text)):
        t = text[:i] + text[i+1:]
        if t == t[::-1]:
            print(t)
            check = False
            break

    if check:
        print("not possible")