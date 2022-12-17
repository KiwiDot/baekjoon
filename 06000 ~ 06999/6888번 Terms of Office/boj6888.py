# 백준 6888번 Terms of Office
import sys
put = sys.stdin.readline

X = int(put())
Y = int(put())

for i in range(X, Y+1, 60):
    print("All positions change in year {}".format(i))