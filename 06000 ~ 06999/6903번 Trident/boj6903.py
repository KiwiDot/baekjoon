# 백준 6903번 Trident
import sys
put = sys.stdin.readline

t = int(put())  # 창의 길이
s = int(put())  # 창 사이의 간격
h = int(put())  # 손잡이의 길이

# 창
for i in range(t):
    print('*' + ' ' * s + '*' + ' ' * s + '*')

# 연결 마디
print('*' * (s * 2 + 3))

# 손잡이
for i in range(h):
    print(' ' * (s+1) + '*')