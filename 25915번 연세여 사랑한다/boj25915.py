# 백준 25915번 연세여 사랑한다
import sys
put = sys.stdin.readline

e = put().strip()

# ILOVEYONSEI의 거리는 총 84
cnt = 84 + abs(ord(e) - ord('I'))
print(cnt)