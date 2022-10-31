# 백준 10551번 STROJOPIS
import sys
put = sys.stdin.readline

keyboard = {0: "`1QAZ", 1: "2WSX", 2: "3EDC", 3: "45RTFGVB",
            4: "67YUHJNM", 5: "8IK,", 6: "9OL.", 7: "0-=P[];'/"}
cnt = [0] * 8

s = put().strip()
for i in s:
    for j in range(8):
        if i in keyboard[j]:
            cnt[j] += 1
            break

for i in cnt:
    print(i)