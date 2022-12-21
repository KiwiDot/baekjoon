# 백준 5356번 Triangles
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    number, letter = put().split()

    for i in range(1, int(number)+1):
        print(letter * i)
        letter = chr((ord(letter) - 64) % 26 + 65)
    print()