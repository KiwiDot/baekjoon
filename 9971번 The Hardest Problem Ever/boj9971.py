# 백준 9971번 The Hardest Problem Ever
import sys
put = sys.stdin.readline

plain = "V W X Y Z A B C D E F G H I J K L M N O P Q R S T U".split()

while True:
    start = put().strip()
    if start == "ENDOFINPUT":
        break

    caesar = list(put().strip())
    end = put().strip()

    for i in range(len(caesar)):
        if caesar[i].isalpha():
            caesar[i] = plain[ord(caesar[i]) - 65]

    print(''.join(caesar))