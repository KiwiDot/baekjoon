# 백준 5249번 Pirates On Parade
import sys
put = sys.stdin.readline

pirates = {}

while True:
    try:
        name, height = put().split()
        pirates[int(height)] = name
    except:
        break

p = 0
for i in sorted(pirates.keys()):
    if not p:
        p = i
    else:
        if i - p <= 2:
            print(pirates[p], pirates[i])
            p = 0
        else:
            p = i
