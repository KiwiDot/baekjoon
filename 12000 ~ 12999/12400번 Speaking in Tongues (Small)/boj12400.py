# 백준 12400번 Speaking in Tongues (Small)
import sys
put = sys.stdin.readline

# Googlerese 매핑 찾기
Googlerese = {'q': 'z', 'z': 'q'}   # z 와 q는 예제에 들어있지 않으나, 서로밖에 안남는다

in1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
in2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
in3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

out1 = "our language is impossible to understand"
out2 = "there are twenty six factorial possibilities"
out3 = "so it is okay if you want to just give up"

in_ = [in1, in2, in3]
out_ = [out1, out2, out3]

for i in range(3):
    for j in range(len(in_[i])):
        if in_[i][j] not in Googlerese:
            Googlerese[in_[i][j]] = out_[i][j]

# 실제 문제
T = int(put())

for t in range(1, T+1):
    G = list(put().strip())
    for i in range(len(G)):
        G[i] = Googlerese[G[i]]
    print("Case #{}: {}".format(t, ''.join(G)))
