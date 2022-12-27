# 백준 24196번 Gömda ord
import sys
put = sys.stdin.readline

alphabet = {}
for i in range(26):
    alphabet[chr(i+65)] = i+1
    alphabet[chr(i+97)] = i+1

text = put().strip()
idx = 0
answer = ""

while idx < len(text):
    answer += text[idx]
    idx += alphabet[text[idx]]

print(answer)