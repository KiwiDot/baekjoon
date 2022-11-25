# 백준 15121번 Star Arrangements
import sys
put = sys.stdin.readline

S = int(put())
print("{}:".format(S))

for x in range(2, S):
    for y in range(x-1, x+1):
        if not S % (x + y) or not (S - x) % (x + y):
            print("{},{}".format(x, y))
