# 백준 5939번 Race Results
import sys
put = sys.stdin.readline

N = int(put())
cow = [put().strip() for i in range(N)]
cow.sort(key=lambda x: int(x.split()[0]) * 10000 + int(x.split()[1]) * 100 + int(x.split()[2]))

for i in cow:
    print(i)