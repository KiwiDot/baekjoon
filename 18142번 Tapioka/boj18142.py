# 백준 18142번 Tapioka
import sys
put = sys.stdin.readline

text = put().split()

for i in range(3):
    if text[i] == "bubble" or text[i] == "tapioka":
        text[i] = ''

answer = ' '.join(text).strip()
print(answer if answer else "nothing")