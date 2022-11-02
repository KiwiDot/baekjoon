# 백준 15122번 Forbidden Zero
import sys
put = sys.stdin.readline

n = str(int(put()) + 1)
print(n.replace('0', '1'))