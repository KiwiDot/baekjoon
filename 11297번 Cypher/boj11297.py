# 백준 11297번 Cypher
import sys
put = sys.stdin.readline

while True:
    key = sum([int(_) for _ in put().split()])
    if not key:
        break
    key = key % 25 + 1
    text = put().strip()
    cyper = {}

    for i in range(26):
        cyper[chr((i+key)%26+97)] = chr(i+97)

    for i in text:
        if i.isalpha():
            i = cyper[i]
        print(i, end='')
    print()