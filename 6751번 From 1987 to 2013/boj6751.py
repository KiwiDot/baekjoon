# 백준 6751번 From 1987 to 2013
import sys
put = sys.stdin.readline

Y = int(put())

while True:
    Y += 1
    if len(set(str(Y))) == len(str(Y)):
        print(Y)
        break