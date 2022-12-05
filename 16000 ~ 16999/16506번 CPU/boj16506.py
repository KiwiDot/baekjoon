# 백준 16506번 CPU
import sys
put = sys.stdin.readline

N = int(put())
opcode = {"ADD": "0000", "SUB": "0001", "MOV": "0010", "AND": "0011",
          "OR": "0100", "NOT": "0101", "MULT": "0110", "LSFTL": "0111",
          "LSFTR": "1000", "ASFTR": "1001", "RL": "1010", "RR": "1011"}

while N:
    N -= 1
    o, rD, rA, r = put().split()
    rB = True
    answer = ""

    # 0 ~ 3
    for i in opcode.keys():
        if i in o:
            if 'C' in o:
                answer += opcode[o[:-1]]
                rB = False
            else:
                answer += opcode[o]
            break

    # 4 ~ 5
    if rB:
        answer += '00'
    else:
        answer += '10'

    # 6 ~ 8
    answer += bin(int(rD))[2:].zfill(3)

    # 9 ~ 11
    if o == "MOV" or o == "MOVC" or o == "NOT":
        answer += "000"
    else:
        answer += bin(int(rA))[2:].zfill(3)

    # 12 ~ 15
    if rB:
        answer += bin(int(r))[2:].zfill(3) + '0'
    else:
        answer += bin(int(r))[2:].zfill(4)

    print(answer)