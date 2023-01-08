# 백준 9507번 Generations of Tribbles
import sys
put = sys.stdin.readline

koong = [1, 1, 2, 4, 8] + [0] * 63
for i in range(5, 68):
    koong[i] = koong[i-1] + koong[i-2] + koong[i-3] + koong[i-4]
t = int(put())

while t:
    t -= 1
    n = int(put())
    print(koong[n])