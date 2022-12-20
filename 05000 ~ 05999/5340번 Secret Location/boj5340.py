# 백준 5340번 Secret Location
import sys
put = sys.stdin.readline

x = [0] + [len(put().strip()) for i in range(6)]
print("Latitude {}:{}:{}".format(x[1], x[2], x[3]))
print("Longitude {}:{}:{}".format(x[4], x[5], x[6]))