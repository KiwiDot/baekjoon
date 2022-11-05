# 백준 11269번 Cryptographer’s Conundrum
import sys
put = sys.stdin.readline

text = put().strip()
t = len(text) // 3
name = "PER" * t
cnt = 0

for i in range(t * 3):
    if text[i] != name[i]:
        cnt += 1

print(cnt)
