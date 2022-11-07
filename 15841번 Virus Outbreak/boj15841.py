# 백준 15841번 Virus Outbreak
import sys
put = sys.stdin.readline
cow = [0, 1, 1, 2, 3]

while True:
    X = int(put())
    if X == -1:
        break

    if X >= len(cow):
        for i in range(len(cow), X+1):
            cow.append(cow[i-2] + cow[i-1])

    print("Hour {}: {} cow(s) affected".format(X, cow[X]))
