# 백준 21867번 Java Bitecode
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()

for i in ['J', 'A', 'V']:
    S = S.replace(i, '')

# JAVA Bitecode의 길이가 0이라면, S는 빈 문자열이 된다.
print(S if S else "nojava")
