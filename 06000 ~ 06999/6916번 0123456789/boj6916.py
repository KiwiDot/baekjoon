# 백준 6916번 0123456789
import sys
put = sys.stdin.readline

n = int(put())

# 세그먼트 1
if n in {0, 2, 3, 5, 6, 7, 8, 9}:
    print(" * * *")
else:
    print()

# 세그먼트 2 ~ 3
if n in {5, 6}:
    star = "*"
elif n in {1, 2, 3, 7}:
    star = "      *"
else:
    star = "*     *"
for i in range(3):
    print(star)

# 세그먼트 4
if n in {0, 1, 7}:
    print()
else:
    print(" * * *")

# 세그먼트 5 ~ 6
if n == 2:
    star = "*"
elif n in {1, 3, 4, 5, 7, 9}:
    star = "      *"
else:
    star = "*     *"
for i in range(3):
    print(star)

# 세그먼트 7
if n in {0, 2, 3, 5, 6, 8, 9}:
    print(" * * *")
else:
    print()