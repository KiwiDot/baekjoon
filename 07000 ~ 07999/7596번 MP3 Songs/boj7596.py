# 백즌 7596번 MP3 Songs
import sys
put = sys.stdin.readline
t = 0

while True:
    t += 1
    n = int(put())
    if not n:
        break
    song = sorted([put().strip() for i in range(n)])

    print(t)
    for i in song:
        print(i)