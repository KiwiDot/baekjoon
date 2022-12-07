# 백준 20114번 미아 노트
import sys
put = sys.stdin.readline

N, H, W = map(int, put().split())
note = ['?' for i in range(N)]

while H:
    H -= 1
    text = put().strip()

    for i in range(0, N * W, W):
        if note[i//W] == '?':
            t = text[i:i+W].replace('?', '')
            if t:
                note[i//W] = t[0]

print(''.join(note))