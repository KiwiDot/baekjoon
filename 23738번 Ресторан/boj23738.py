# 백준 23738번 Ресторан
import sys
put = sys.stdin.readline

char = {'A': 'a', 'B': 'v', 'E': 'ye', 'K': 'k', 'M': 'm', 'H': 'n',
        'O': 'o', 'P': 'r', 'C': 's', 'T': 't', 'Y': 'u', 'X': 'h'}
word = put().strip()

for i in char.keys():
    word = word.replace(i, char[i])

print(word)