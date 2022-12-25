# 백준 26768번 H4x0r
import sys
put = sys.stdin.readline

Litera = ['a', 'e', 'i', 'o', 's']
Cyfra = ['4', '3', '1', '0', '5']
text = put().strip()

for i in range(5):
    text = text.replace(Litera[i], Cyfra[i])

print(text)