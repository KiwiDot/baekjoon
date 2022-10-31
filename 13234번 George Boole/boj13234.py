# 백준 13234번 George Boole
import sys
put = sys.stdin.readline

s = put().strip()

if "AND" in s:
    s = s.split(" AND ")
    s[0] = True if s[0] == "true" else False
    s[1] = True if s[1] == "true" else False
    print("true" if s[0] & s[1] else "false")

else:
    s = s.split(" OR ")
    s[0] = True if s[0] == "true" else False
    s[1] = True if s[1] == "true" else False
    print("true" if s[0] | s[1] else "false")