# 백준 6438번 Reverse Text
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    text = put().strip()
    print(text[::-1])