# 백준 9954번 Cedric's Cypher
import sys
put = sys.stdin.readline

while True:
    text = put().strip()
    if text == '#':
        break
    s = ord(text[-1]) - 65

    for i in text[:-1]:
        if i.isalpha():
            if i.isupper():
                i = chr(ord(i) - s) if ord(i) - s >= 65 else chr(ord(i) - s + 26)

            else:
                i = chr(ord(i) - s) if ord(i) - s >= 97 else chr(ord(i) - s + 26)

        print(i, end='')
    print()