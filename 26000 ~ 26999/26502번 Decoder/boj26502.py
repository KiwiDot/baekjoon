# 백준 26502번 Decoder
import sys
put = sys.stdin.readline

n = int(put())
decoder = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'y', 'y': 'a',
           'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'Y', 'Y': 'A'}

while n:
    n -= 1
    text = list(put().strip())

    for i in range(len(text)):
        if text[i] in decoder:
            text[i] = decoder[text[i]]

    print(''.join(text))