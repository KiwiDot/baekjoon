# 백준 23627번 driip
import sys
put = sys.stdin.readline

S = put().strip()

if S[-5:] == "driip":
    print("cute")

else:
    print("not cute")