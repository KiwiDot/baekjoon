# 백준 11608번 Complexity
import sys
put = sys.stdin.readline

text = put().strip()
cnt = [0] * 26

for i in text:
    cnt[ord(i) - 97] += 1
cnt.sort(reverse=True)

answer = len(text) - cnt[0] - cnt[1]
print(answer)