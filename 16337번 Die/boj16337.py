# 백준 16337번 Die
import sys
put = sys.stdin.readline

die1 = put().strip()
die2 = put().strip()
die3 = put().strip()

if die1 == ":::" and die2 == ":o:" and die3 == ":::":
    print(1)

elif die1 == "::o" and die2 == ":::" and die3 == "o::":
    print(2)

elif die1 == "o::" and die2 == ":::" and die3 == "::o":
    print(2)

elif die1 == "::o" and die2 == ":o:" and die3 == "o::":
    print(3)

elif die1 == "o::" and die2 == ":o:" and die3 == "::o":
    print(3)

elif die1 == "o:o" and die2 == ":::" and die3 == "o:o":
    print(4)

elif die1 == "o:o" and die2 == ":o:" and die3 == "o:o":
    print(5)

elif die1 == "ooo" and die2 == ":::" and die3 == "ooo":
    print(6)

elif die1 == "o:o" and die2 == "o:o" and die3 == "o:o":
    print(6)

else:
    print("unknown")