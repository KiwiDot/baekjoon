# 백준 4446번 ROT13

ROT13 = {}
alphabet1 = "aiyeou"
alphabet2 = "bkxznhdcwgpvjqtsrlmf"

for i in range(6):
    ROT13[alphabet1[i]] = alphabet1[i - 3]
    ROT13[alphabet1[i].upper()] = alphabet1[i - 3].upper()

for i in range(20):
    ROT13[alphabet2[i]] = alphabet2[i - 10]
    ROT13[alphabet2[i].upper()] = alphabet2[i - 10].upper()

while True:
    try:
        text = list(input())
        for i in range(len(text)):
            if text[i].isalpha():
                text[i] = ROT13[text[i]]

        print(''.join(text))

    except EOFError:
        break