# 백준 23367번 Dickensian Dictionary
import sys
put = sys.stdin.readline

text = list(put().strip())
left = set("qwertasdfgzxcvb")
right = set("yuiophjklnm")

for i in range(len(text)):
    if text[i] in left:
        text[i] = '1'
    else:
        text[i] = '0'
text = ''.join(text)

if '00' in text or '11' in text:
    print("no")
else:
    print("yes")