# 백준 17039번 Sleepy Cow Herding (Bronze)
import sys
put = sys.stdin.readline

c1, c2, c3 = sorted([int(_) for _ in put().split()])

# 최솟값
if c1 == c2 - 1 and c3 == c2 + 1:
    print(0)
elif c2 - c1 == 2 or 0 < c3 - c2 == 2:
    print(1)
else:
    print(2)

# 최댓값
print(max(c2 - c1 - 1, c3 - c2 - 1))