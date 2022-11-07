# 백준 7366번 Counting Sheep
import sys
put = sys.stdin.readline

n = int(put())

for i in range(1, n+1):
    m = int(put())
    word = put().split()

    print("Case {}: This list contains {} sheep.".format(i, word.count("sheep")))
    print()