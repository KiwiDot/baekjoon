# 백준 15874번 Caesar Cipher
import sys
put = sys.stdin.readline

k, s = map(int, put().split())
S = put().strip()
answer = ""

for i in S:
    if i == ' ' or i == '.' or i == ',':
        answer += i
        continue

    s = ord(i)
    if 65 <= s <= 90:
        s = chr(((s - 65) + k) % 26 + 65)
    else:
        s = chr(((s - 97) + k) % 26 + 97)

    answer += s

print(answer)