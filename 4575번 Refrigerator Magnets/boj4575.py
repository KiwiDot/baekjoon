# 백준 4575번 Refrigerator Magnets
import sys
put = sys.stdin.readline

while True:
    word = put().strip()
    if word == "END":
        break

    w = word.replace(' ', '')
    if len(w) == len(set(w)):
        print(word)