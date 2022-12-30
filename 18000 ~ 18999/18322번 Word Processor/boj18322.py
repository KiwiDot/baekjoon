# 백준 18322번 Word Processor
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
text = put().split()
cnt = 0
answer = []

for i in range(N):
    if cnt + len(text[i]) > K:
        print(' '.join(answer))
        cnt = len(text[i])
        answer = [text[i]]

    else:
        cnt += len(text[i])
        answer += [text[i]]

print(' '.join(answer))