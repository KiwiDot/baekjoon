# 백준 15444번 Vera and ABCDE
import sys
put = sys.stdin.readline

ABCDE = {'A': ['***', '*.*', '***', '*.*', '*.*'],
         'B': ['***', '*.*', '***', '*.*', '***'],
         'C': ['***', '*..', '*..', '*..', '***'],
         'D': ['***', '*.*', '*.*', '*.*', '***'],
         'E': ['***', '*..', '***', '*..', '***']}

N = int(put())
S = put().strip()

for i in range(5):
    for s in S:
        print(ABCDE[s][i], end='')
    print()