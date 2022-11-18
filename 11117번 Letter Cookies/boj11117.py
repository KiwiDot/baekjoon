# 백준 11117번 Letter Cookies
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    W = put().strip()
    AZ = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
          'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for i in W:
        AZ[i] += 1

    box = int(put())
    while box:
        box -= 1
        word = put().strip()
        az = {}
        for i in word:
            if i in az:
                az[i] += 1
            else:
                az[i] = 1

        check = True
        for i in az.keys():
            if az[i] > AZ[i]:
                check = False
                break

        if check:
            print("YES")
        else:
            print("NO")
