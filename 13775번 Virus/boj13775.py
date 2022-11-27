# 백준 13775번 Virus
import sys
put = sys.stdin.readline

K = int(put())
text = list(put().strip())

for i in range(len(text)):
    if text[i].isalpha():
        t = ord(text[i]) - 97 - K if ord(text[i]) > 97 + K else ord(text[i]) - 71 - K
        text[i] = chr(t % 26 + 97)
        K += 1
        if K > 25:
            K = 1

print(''.join(text))